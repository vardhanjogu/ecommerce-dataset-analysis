import csv

# Load users
users = []
with open('users.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = {
            "id": int(row["id"]),
            "name": f"{row.get('first_name', '').strip()} {row.get('last_name', '').strip()}"
        }
        users.append(user)

# Load orders
orders = []
with open('orders.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        order = {
            "order_id": int(row["order_id"]),
            "user_id": int(row["user_id"]),
            # Add more fields if you need them
        }
        orders.append(order)
