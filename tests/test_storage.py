"""
Unit tests for the SpendLog storage module.
"""

import unittest
import os
import tempfile
import shutil
from spendlog.storage import ExpenseStorage


class TestExpenseStorage(unittest.TestCase):
    """Test cases for ExpenseStorage class."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_expenses.csv")
        self.storage = ExpenseStorage(self.test_file)
    
    def tearDown(self):
        """Clean up test environment."""
        # Remove the temporary directory and all its contents
        shutil.rmtree(self.test_dir)
    
    def test_save_and_load_expense(self):
        """Test saving and loading a single expense."""
        expense = {
            "date": "2023-01-01",
            "category": "Food",
            "description": "Lunch",
            "amount": "15.50"
        }
        
        # Save the expense
        self.storage.save_expense(expense)
        
        # Load expenses and verify
        expenses = self.storage.load_expenses()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0], expense)
    
    def test_load_empty_file(self):
        """Test loading expenses from an empty file."""
        expenses = self.storage.load_expenses()
        self.assertEqual(expenses, [])
    
    def test_get_total_spent(self):
        """Test calculating total amount spent."""
        # Save multiple expenses
        expenses = [
            {"date": "2023-01-01", "category": "Food", "description": "Lunch", "amount": "15.50"},
            {"date": "2023-01-02", "category": "Transport", "description": "Bus fare", "amount": "2.75"},
            {"date": "2023-01-03", "category": "Entertainment", "description": "Movie", "amount": "12.00"}
        ]
        
        for expense in expenses:
            self.storage.save_expense(expense)
        
        # Check total
        total = self.storage.get_total_spent()
        self.assertEqual(total, 30.25)


if __name__ == "__main__":
    unittest.main()