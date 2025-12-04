"""
Storage module for SpendLog expense tracker.
Handles saving and loading expense data from CSV files.
"""

import csv
import os
from typing import List, Dict


class ExpenseStorage:
    """Handles expense data storage in CSV format."""
    
    def __init__(self, filepath: str = "data/expenses.csv"):
        self.filepath = filepath
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        
    def save_expense(self, expense: Dict[str, str]) -> None:
        """Save a single expense to the CSV file."""
        # Check if file exists to determine if we need to write headers
        file_exists = os.path.isfile(self.filepath) and os.path.getsize(self.filepath) > 0
        
        # Handle UTF-16 encoded files
        if file_exists:
            # Check encoding
            with open(self.filepath, 'rb') as f:
                header = f.read(2)
                if header == b'\xff\xfe':
                    encoding = 'utf-16'
                else:
                    encoding = 'utf-8'
        else:
            encoding = 'utf-8'
        
        # Ensure the file ends with a newline before appending
        if file_exists:
            with open(self.filepath, 'rb+') as f:
                f.seek(-1, 2)  # Go to the last byte
                if f.read(1) != b'\n':
                    f.write(b'\n')
        
        with open(self.filepath, mode='a', newline='', encoding=encoding) as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'description', 'amount'])
            
            # Write header if this is a new file
            if not file_exists:
                writer.writeheader()
                
            writer.writerow(expense)
    
    def load_expenses(self) -> List[Dict[str, str]]:
        """Load all expenses from the CSV file."""
        expenses = []
        
        if not os.path.isfile(self.filepath) or os.path.getsize(self.filepath) == 0:
            return expenses
            
        # Detect encoding
        with open(self.filepath, 'rb') as f:
            header = f.read(2)
            if header == b'\xff\xfe':
                encoding = 'utf-16'
            else:
                encoding = 'utf-8'
            
        with open(self.filepath, mode='r', encoding=encoding) as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Only add rows that have the required fields
                if 'date' in row and 'category' in row and 'description' in row and 'amount' in row:
                    expenses.append(row)
            
        return expenses
    
    def get_total_spent(self) -> float:
        """Calculate the total amount spent."""
        expenses = self.load_expenses()
        total = 0.0
        for expense in expenses:
            try:
                total += float(expense['amount'])
            except (ValueError, KeyError):
                # Skip invalid entries
                continue
        return total