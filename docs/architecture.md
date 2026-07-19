## 🏛️ System Architecture (How It Works)
Our application is split into three main components that work together over the internet:

   1. The Code Repository (GitHub): Holds all our raw Python files safely online.
   2. The Frontend Engine (Streamlit): Hosts and calculates our trading logic on a cloud server and renders the beautiful dashboard webpage for students.
   3. The Database (Supabase): Acts as our secure "source of truth." It stores all student balances, stock portfolios, and past order records safely.

------------------------------
## 📦 File Structure (Where Code Lives)
To keep the application neat, we separate tasks into different files so we don't make one giant, confusing script:

* main.py: The visual layer. It controls what the student sees on their screen (buttons, input boxes, tables, and graphs).
* storage.py: The data courier. It contains simple commands to save data to Supabase or pull data out of it.
* user.py: The wallet supervisor. It tracks user profiles and makes sure a student has enough virtual cash before allowing a trade.
* order_book.py: The transaction log. It records when students want to buy or sell a stock and marks them as PENDING.
* matching_engine.py: The math brain. It matches student buy/sell orders against our stock prices.

------------------------------
## 🗄️ Database Tables (How Data is Organized)
We store our information inside 5 core tables inside Supabase:

   1. profiles: Stores the student's username and their virtual cash balance (everyone starts with a practice pool of $100,000.00).
   2. portfolio: An inventory list tracking exactly what stock shares each student currently owns (e.g., 10 shares of AAPL).
   3. order_book: Holds open buy and sell limit orders that are waiting for prices to match.
   4. live_market_prices: A tiny table that holds the latest price for each stock we track.
   5. trade_history: A receipt archive that logs every successful trade completed by students.

------------------------------
## ⚙️ Core Platform Features## 1. Simple Signup & Login
Students create an account using their school email and a password. Thanks to custom settings, email confirmation is disabled, so accounts work instantly!
## 2. The Hybrid Price Engine (Smart Trading)
To keep the game exciting while preventing our system from getting blocked by external data sources, we use a hybrid pricing trick:

* Real Data: Every 1 hour, the system fetches the official, live stock price from the real stock market.
* Simulated Data: Between those hours, every time a student interacts with the page, the system fluctuates the price randomly by a tiny amount (between -0.5% and +0.5%). This gives a fun, fast video-game feel!

## 3. "Lazy Matching" System
We do not run an expensive 24/7 background server. Instead, our matching engine runs on-demand. The microsecond a student clicks any button or loads the dashboard page, Streamlit quickly processes the trades in the background before rendering the screen.
## 4. Daily 5:00 PM Market Settlement
At 5:00 PM every day, a GitHub Actions Cron Job automatically wakes up our system to run the official "End of Day" routine:

   1. It runs a final price match check.
   2. It cancels any leftover PENDING orders so the order book is completely clean for the next morning.
   3. It deletes transaction receipts older than 30 days to save space on our free database plan.

------------------------------
## 🛡️ Built-in Safety & Security
Even though this is an open-source student app, it is highly secure:

* No Rounding Errors: We use financial-grade data storage (NUMERIC) so we never lose fractional pennies.
* Anti-Cheat Constraints: The database itself has a hard rule stating cash_balance >= 0. Even if a bug occurs in Python, a student can physically never trick the platform into giving them negative debt to buy endless shares.
* Server-Side Execution: All code runs hidden away on Streamlit and Supabase cloud servers. Students only receive the final visual website, meaning they cannot change the price values or cheat from their browsers.

------------------------------
## 🚀 Proceeding to Code Implementation
This documentation perfectly reflects the entire blueprints of your trading platform!
