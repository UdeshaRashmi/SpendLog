import csv

# Create a new CSV file with proper UTF-8 encoding
with open('data/expenses.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['date', 'category', 'description', 'amount'])

print("CSV file created successfully!")