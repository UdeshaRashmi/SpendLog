from spendlog.storage import ExpenseStorage

# Test the storage module directly
storage = ExpenseStorage()

print("Loading expenses...")
expenses = storage.load_expenses()
print(f"Loaded {len(expenses)} expenses")

print("Getting total...")
total = storage.get_total_spent()
print(f"Total spent: ${total}")

print("Adding a test expense...")
test_expense = {
    "date": "2023-12-04",
    "category": "Direct Test",
    "description": "Testing storage module directly",
    "amount": "25.00"
}

try:
    storage.save_expense(test_expense)
    print("Expense added successfully!")
except Exception as e:
    print(f"Error adding expense: {e}")

print("Loading expenses again...")
expenses = storage.load_expenses()
print(f"Loaded {len(expenses)} expenses")

print("Getting total again...")
total = storage.get_total_spent()
print(f"Total spent: ${total}")

print("All expenses:")
for expense in expenses:
    print(f"  {expense}")