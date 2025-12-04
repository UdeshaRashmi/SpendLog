# 🧾 SpendLog - Expense Tracker

A beginner-friendly Python project that helps you record daily expenses and view your total spending. The app stores all expense entries in a CSV file and provides a simple command-line interface to add new expenses, list all records, and calculate totals.

## 🔍 Features

- Add expenses with date, category, description, and amount
- Automatically save data into a CSV file
- View all recorded expenses in a clean table
- See the total amount spent
- Beginner-friendly project structure using Python & VS Code

## 🛠️ Technologies Used

- Python 3
- CSV file handling
- Command Line Interface (CLI)
- VS Code

## 🚀 Getting Started

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: 
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python -m spendlog.cli`

## 📁 Project Structure

```
SpendLog/
├─ .venv/                 # Virtual environment (not included in repo)
├─ data/
│  └─ expenses.csv        # Created by app
├─ spendlog/
│  ├─ __init__.py
│  ├─ cli.py
│  └─ storage.py
├─ tests/
│  └─ test_storage.py
├─ .gitignore
├─ requirements.txt
└─ README.md
```