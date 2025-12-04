import requests
import json

# Test GET request
print("Testing GET /api/expenses...")
response = requests.get("http://127.0.0.1:5000/api/expenses")
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"Expenses: {len(data['expenses'])}")
    print(f"Total: ${data['total']}")

# Test POST request
print("\nTesting POST /api/expenses...")
expense_data = {
    "date": "2023-12-04",
    "category": "API Test",
    "description": "Testing API endpoint",
    "amount": 15.50
}

response = requests.post(
    "http://127.0.0.1:5000/api/expenses",
    headers={"Content-Type": "application/json"},
    data=json.dumps(expense_data)
)

print(f"Status Code: {response.status_code}")
if response.status_code == 201:
    data = response.json()
    print(f"Message: {data['message']}")