"""
Tests for the storage module of SpendLog.
"""

import os
import tempfile
import unittest
from datetime import datetime

from spendlog.storage import ExpenseStorage


class TestExpenseStorage(unittest.TestCase):
    """Test cases for the ExpenseStorage class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        self.temp_file.close()
        self.storage = ExpenseStorage(self.temp_file.name)
    
    def tearDown(self):
        """Clean up test fixtures."""
        # Remove the temporary file
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_save_and_load_expense(self):
        """Test saving and loading a single expense."""
        expense = {
            'date': '2023-01-01',
            'category': 'Food',
            'description': 'Lunch',
            'amount': '15.50'
        }
        
        # Save the expense
        self.storage.save_expense(expense)
        
        # Load expenses and check
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
            {'date': '2023-01-01', 'category': 'Food', 'description': 'Lunch', 'amount': '15.50'},
            {'date': '2023-01-02', 'category': 'Transport', 'description': 'Bus fare', 'amount': '2.50'},
            {'date': '2023-01-03', 'category': 'Entertainment', 'description': 'Movie', 'amount': '12.00'}
        ]
        
        for expense in expenses:
            self.storage.save_expense(expense)
        
        # Check total
        total = self.storage.get_total_spent()
        self.assertEqual(total, 30.0)  # 15.50 + 2.50 + 12.00
    
    def test_get_total_spent_empty(self):
        """Test calculating total when no expenses exist."""
        total = self.storage.get_total_spent()
        self.assertEqual(total, 0.0)


if __name__ == '__main__':
    unittest.main()