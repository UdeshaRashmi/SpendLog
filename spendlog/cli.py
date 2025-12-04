"""
Command-line interface for SpendLog expense tracker.
Provides user interaction for adding, viewing, and analyzing expenses.
"""

import sys
from datetime import datetime
from typing import Dict

from spendlog.storage import ExpenseStorage


def get_user_input(prompt: str) -> str:
    """Get input from user with prompt."""
    return input(f"{prompt}: ").strip()


def get_expense_data() -> Dict[str, str]:
    """Collect expense data from user."""
    print("\n--- Add New Expense ---")
    
    # Get date (default to today)
    date_str = get_user_input("Date (YYYY-MM-DD) [today]")
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Validate date format
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Using today's date.")
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    category = get_user_input("Category")
    description = get_user_input("Description")
    
    # Get amount and validate
    while True:
        amount_str = get_user_input("Amount")
        try:
            float(amount_str)
            break
        except ValueError:
            print("Please enter a valid number for amount.")
    
    return {
        "date": date_str,
        "category": category,
        "description": description,
        "amount": amount_str
    }


def display_expenses(storage: ExpenseStorage) -> None:
    """Display all expenses in a formatted table."""
    expenses = storage.load_expenses()
    
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    print("\n--- All Expenses ---")
    print(f"{'Date':<12} {'Category':<15} {'Description':<30} {'Amount':<10}")
    print("-" * 70)
    
    for expense in expenses:
        print(f"{expense['date']:<12} {expense['category']:<15} {expense['description']:<30} ${float(expense['amount']):<9.2f}")
    
    total = storage.get_total_spent()
    print("-" * 70)
    print(f"{'TOTAL SPENT:':<57} ${total:<9.2f}")


def main_menu(storage: ExpenseStorage) -> None:
    """Display main menu and handle user choices."""
    while True:
        print("\n--- SpendLog Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Exit")
        
        choice = get_user_input("Select an option (1-4)")
        
        if choice == "1":
            expense = get_expense_data()
            storage.save_expense(expense)
            print("Expense saved successfully!")
        elif choice == "2":
            display_expenses(storage)
        elif choice == "3":
            total = storage.get_total_spent()
            print(f"\nTotal Spent: ${total:.2f}")
        elif choice == "4":
            print("Thank you for using SpendLog!")
            sys.exit(0)
        else:
            print("Invalid option. Please select 1-4.")


def main():
    """Main entry point for the application."""
    storage = ExpenseStorage()
    main_menu(storage)


if __name__ == "__main__":
    main()