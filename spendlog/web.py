"""
Web interface for SpendLog expense tracker.
Provides a web-based UI to add expenses, list expenses, and show total spending.
"""

import os
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from spendlog.storage import ExpenseStorage

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Set the template directory to the templates folder in the project root
template_dir = os.path.join(os.path.dirname(current_dir), 'templates')

app = Flask(__name__, template_folder=template_dir)
storage = ExpenseStorage()

@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    """Return all expenses as JSON."""
    expenses = storage.load_expenses()
    total = storage.get_total_spent()
    return jsonify({
        'expenses': expenses,
        'total': total
    })

@app.route('/api/expenses', methods=['POST'])
def add_expense_api():
    """Add a new expense via API."""
    try:
        # Get JSON data
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['date', 'category', 'description', 'amount']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Create expense dictionary
        expense = {
            "date": data['date'],
            "category": data['category'],
            "description": data['description'],
            "amount": str(data['amount'])
        }
        
        # Save expense
        storage.save_expense(expense)
        
        return jsonify({'message': 'Expense saved successfully!', 'expense': expense}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/total')
def get_total():
    """Return total amount spent."""
    total = storage.get_total_spent()
    return jsonify({'total': total})

@app.route('/expenses')
def list_expenses():
    """Display all expenses in a table."""
    expenses = storage.load_expenses()
    total = storage.get_total_spent()
    return render_template('expenses.html', expenses=expenses, total=total)

@app.route('/total')
def show_total():
    """Display total amount spent."""
    total = storage.get_total_spent()
    return render_template('total.html', total=total)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)