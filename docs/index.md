
## 📈 QUNEX: Custom Stock Trading Platform

QUNEX is a lightweight, open-source virtual stock market trading platform built specifically for educational purposes, strategy testing, and fintech research. It allows users to simulate real-market environments using 100% virtual practice money ($10,000.00 starting balance) with zero financial risk.

------------------------------

## 🎯 Target Audience & Use Cases
QUNEX is uniquely built to serve three core audiences:

* 1. Students & Beginners: Get an authentic, real-time trading experience. Learn how order books work, practice risk management, and understand portfolio dynamics before committing real money to live stock exchanges.

* 2. Active Traders: Backtest custom manual strategies or practice tape reading within a safe, sandboxed market playground.

* 3. Researchers & Fintech Engineers: Leverage the platform's clean data structures to train machine learning models, test algorithmic trading concepts, or run quantitative research simulations.

------------------------------
## 🏎️ Key Project Constraints

* Asset Pool: To keep the trading ecosystem highly focused, clean, and lightning-fast, QUNEX launches tracking exactly 10 major companies (e.g., AAPL, NVDA, TSLA, MSFT).

* 100% Virtual Practice Money: The platform uses financial-grade tracking for mock credits. No real currency is ever accepted, deposited, or traded.

------------------------------
## 🧠 The Hybrid Price Model
To prevent our cloud systems from hitting strict API rate limits or getting blocked by external data providers, QUNEX utilizes a smart Hybrid Pricing Engine:

   1. Real Market Benchmarks: Every 1 hour, the core backend fetches official, real-time stock price data from the actual stock market.

   2. Gamified Micro-Movements: Between those hourly updates, every time a student loads a dashboard or clicks an interaction button, the system introduces a tiny, random price fluctuation (between -0.5% and +0.5%).

This hybrid approach creates an active, high-speed, video-game-like environment for classroom hours while keeping external data requests completely safe and free.

------------------------------

## 🏛️ System Architecture

This section details how the platform modules interact. You can update this structural map as development progresses.

     [ Streamlit GUI Frontend ] (main.py)
                 │
                 ▼
     [ Core Modular Business Logic ]
  ┌──────────────┴──────────────┐
  ▼                             ▼
(user.py / order_book.py)   (matching_engine.py)
  │                             │
  └──────────────┬──────────────┘
                 ▼
     [ Data Storage Layer ] (storage.py)
                 │
                 ▼
     [ Supabase Cloud Database ] (Profiles, Portfolios, Orders)

## Module Responsibilities:

* main.py: The central orchestrator. It manages all user interface layouts, buttons, metric displays, and graphs.
* storage.py: The database data courier. It houses pure functions that read from and write to our Supabase tables.
* user.py: The portfolio supervisor. Tracks student profiles and performs capital validation checks.
* order_book.py: The transaction log. Manages order creation requests and captures active customer intent.
* matching_engine.py: The calculation engine. Matches open client transactions against the active hybrid price feed.

------------------------------
## 🧭 Documentation Navigation Roadmaps

To navigate through the architecture guides, pick a section from your menu panel:
*   **⚙️ Core Modules ([Core Modules](architecture.md))**:Explore our deep technical blueprints, including [Database Blueprints](core_module/database_structure.md) for table schemas and [Matching Engine Logic](core_module/matching_engine.md) for execution formulas.


*   **📜 Project Updates ([Changelog](changelog.md))**: Check chronological update listings, feature additions, bug resolution histories, and platform optimizations.

*   **🎯 Project Roadmaps ([Milestones](milestones.md))**: Monitor our phase development tracker from basic cloud schema installations to automated cloud deployment configurations.

*   **🤝 Open Source Hall ([Contributors](contributors.md))**: Meet our maintainers and code contributors, or read instructions on how to submit code optimizations via GitHub Pull Requests.

------------------------------


## ⚙️ Quick Start Installation
Want to run this platform locally on your machine? Follow these simple commands:
## 1. Clone the project files

git clone https://github.com/Krishna3112Y/QUNEX
cd qunex

## 2. Install Python dependencies

pip install -r requirements.txt

## 3. Launch the web dashboard

streamlit run main.py

