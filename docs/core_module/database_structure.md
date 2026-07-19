# 🗄️ Core Database Blueprints & Table Structures

QUNEX uses a managed **Supabase Postgres** instance to track player records, portfolios, and real-time ledger histories. Below are the precise technical field specs and safety rules implemented inside our relational database.

---

## 1. `profiles` Table
Stores student identity parameters and accounts metrics.

| Field Name | Data Type | Key Type | Default Value | Validation/Safety Rules |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | **Primary Key** | *None* | Must match the Supabase `auth.users` registration token |
| `username` | `TEXT` | **Unique Constraint**| *None* | Cannot be duplicated; identifies student on leaderboards |
| `cash_balance`| `NUMERIC(15,2)`| *None* | `100000.00` | **CHECK `cash_balance >= 0`** (Prevents illegal overdrafts) |
| `created_at` | `TIMESTAMP` | *None* | `NOW()` | Records exact account creation time automatically |

---

## 2. `portfolio` Table
Tracks asset inventory balances. A student cannot hold duplicate stock rows.

| Field Name | Data Type | Key Type | Default Value | Validation/Safety Rules |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `BIGSERIAL` | **Primary Key** | *Auto-Increment*| Unique sequence tracker code |
| `user_id` | `UUID` | **Foreign Key** | *None* | Cascade deletes if a student profile is removed |
| `ticker` | `VARCHAR(10)`| *None* | *None* | Always forced to UPPERCASE tokens (e.g., `AAPL`) |
| `shares_owned`| `INT` | *None* | `0` | **CHECK `shares_owned >= 0`** (Cannot short stocks) |

---

## 3. `order_book` Table
Maintains outstanding public transaction requests.

| Field Name | Data Type | Key Type | Default Value | Validation/Safety Rules |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `BIGSERIAL` | **Primary Key** | *Auto-Increment*| Unique order confirmation receipt id |
| `user_id` | `UUID` | **Foreign Key** | *None* | Connects transaction back to author profile |
| `ticker` | `VARCHAR(10)`| *None* | *None* | Target asset name symbol |
| `order_type` | `TEXT` | *None* | *None* | **CHECK `order_type IN ('BUY', 'SELL')`** |
| `price` | `NUMERIC(10,2)`| *None* | *None* | **CHECK `price > 0`** (No negative prices allowed) |
| `quantity` | `INT` | *None* | *None* | **CHECK `quantity > 0`** (No negative share sizing) |
| `status` | `TEXT` | *None* | `'PENDING'` | **CHECK status IN ('PENDING', 'FILLED', 'CANCELLED')** |
