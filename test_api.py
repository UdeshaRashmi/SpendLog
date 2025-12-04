import requests
import json

# Test data
expense_data = {
    "date": "2023-12-04",
    "category": "API Test",
    "description": "Testing API endpoint",
    "amount": 15.50
}

# Send POST request to add expense
response = requests.post(
    "http://127.0.0.1:5000/api/expenses",
    headers={"Content-Type": "application/json"},
    data=json.dumps(expense_data)
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")