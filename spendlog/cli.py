"""
Command-line interface for SpendLog expense tracker.
Provides commands to add expenses, list expenses, and show total spending.
"""

import sys
from datetime import datetime
from typing import Dict

from .storage import ExpenseStorage


def get_current_date() -> str:
    """Get current date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")


def add_expense(storage: ExpenseStorage) -> None:
    """Prompt user for expense details and save to storage."""
    print("\n=== Add New Expense ===")
    
    # Get expense details from user
    date = input(f"Date (YYYY-MM-DD) [{get_current_date()}]: ").strip()
    if not date:
        date = get_current_date()
    
    category = input("Category: ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Category: ").strip()
    
    description = input("Description: ").strip()
    while not description:
        print("Description cannot be empty.")
        description = input("Description: ").strip()
    
    amount_str = input("Amount: ").strip()
    while not amount_str:
        print("Amount cannot be empty.")
        amount_str = input("Amount: ").strip()
    
    try:
        amount = float(amount_str)
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    # Create expense dictionary
    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": str(amount)
    }
    
    # Save expense
    storage.save_expense(expense)
    print("Expense saved successfully!")


def list_expenses(storage: ExpenseStorage) -> None:
    """Display all expenses in a formatted table."""
    print("\n=== All Expenses ===")
    
    expenses = storage.load_expenses()
    
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    # Print table header
    print(f"{'Date':<12} {'Category':<15} {'Description':<30} {'Amount':<10}")
    print("-" * 70)
    
    # Print each expense
    for expense in expenses:
        print(f"{expense['date']:<12} {expense['category']:<15} {expense['description']:<30} ${float(expense['amount']):<9.2f}")
    
    # Print total
    total = storage.get_total_spent()
    print("-" * 70)
    print(f"{'Total Spent:':<57} ${total:<9.2f}")


def show_help() -> None:
    """Display help information."""
    print("\n=== SpendLog - Expense Tracker ===")
    print("Commands:")
    print("  add    - Add a new expense")
    print("  list   - List all expenses")
    print("  total  - Show total spending")
    print("  help   - Show this help message")
    print("  exit   - Exit the application")


def show_total(storage: ExpenseStorage) -> None:
    """Display total amount spent."""
    total = storage.get_total_spent()
    print(f"\n=== Total Spending ===")
    print(f"Total Amount Spent: ${total:.2f}")


def main() -> None:
    """Main entry point for the SpendLog CLI."""
    storage = ExpenseStorage()
    
    print("Welcome to SpendLog - Expense Tracker!")
    show_help()
    
    while True:
        try:
            command = input("\nEnter command (add/list/total/help/exit): ").strip().lower()
            
            if command == "add":
                add_expense(storage)
            elif command == "list":
                list_expenses(storage)
            elif command == "total":
                show_total(storage)
            elif command == "help":
                show_help()
            elif command == "exit":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Unknown command. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()