import streamlit as st
from supabase import create_client, Client

# --- 1. ESTABLISH DATABASE CONNECTION ---
@st.cache_resource
def init_supabase() -> Client:
    """Initializes and caches the Supabase connection client."""
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"❌ Failed to load secrets or connect to database: {e}")
        st.stop()

supabase: Client = init_supabase()

# --- 2. AUTHENTICATION UI LAYER ---
def show_auth_portal():
    st.title("🏦 Database Connection Test Portal")
    st.caption("Verifying real-time auth synchronization between Streamlit and Supabase.")
    st.divider()

    # Layout tabs for switching modes
    tab_login, tab_signup = st.tabs(["🔑 Sign In", "📝 Create Account"])

    # --- TAB A: USER LOGIN ---
    with tab_login:
        st.subheader("Login Credentials")
        with st.form("login_form"):
            email = st.text_input("Email Address", placeholder="student@university.edu")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            login_btn = st.form_submit_button("Test Login Connection", use_container_width=True)

            if login_btn:
                if not email or not password:
                    st.warning("Please fill in both fields.")
                else:
                    try:
                        # Attempt live authentication read from Supabase auth.users
                        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
                        
                        # Store session identifiers on success
                        st.session_state.authenticated = True
                        st.session_state.user_email = response.user.email
                        st.session_state.user_id = response.user.id
                        
                        st.success("✅ Connection Successful! User authenticated.")
                        st.balloons()
                        st.rerun()
                    except Exception as error:
                        st.error(f"❌ Authentication Rejected: {error}")

    # --- TAB B: USER REGISTRATION ---
    with tab_signup:
        st.subheader("Register New Account")
        with st.form("signup_form"):
            new_email = st.text_input("Email Address", placeholder="student@university.edu", key="reg_email")
            # FIXED: Changed non-existent password_input functions to text_input with password type
            new_password = st.text_input("Create Password (min 6 chars)", type="password", placeholder="••••••••", key="reg_pass")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="••••••••", key="reg_conf")
            signup_btn = st.form_submit_button("Test Database Signup", use_container_width=True)

            if signup_btn:
                if not new_email or not new_password:
                    st.warning("All fields are required.")
                elif new_password != confirm_password:
                    st.error("Passwords do not match.")
                else:
                    try:
                        # Attempt to write a new user entry to Supabase
                        response = supabase.auth.sign_up({"email": new_email, "password": new_password})
                        
                        if response.user:
                            st.success("🎉 Success! User record created in Supabase.")
                            st.info("You can now switch over to the Sign In tab to log in.")
                    except Exception as error:
                        st.error(f"❌ Database Write Failed: {error}")

# --- 3. LOCAL TESTING EXECUTION GUARD ---
if __name__ == "__main__":
    # If run directly via streamlit run, initialize local test states
    st.set_page_config(page_title="Auth Connection Test", layout="centered")
    
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        show_auth_portal()
    else:
        st.success(f"Logged in securely as: {st.session_state.user_email}")
        st.write(f"Supabase UID token: `{st.session_state.user_id}`")
        if st.button("Log out"):
            supabase.auth.sign_out()
            st.session_state.authenticated = False
            st.rerun()
