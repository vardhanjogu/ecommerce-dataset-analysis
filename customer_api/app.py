from flask import Flask, jsonify
import csv
from collections import defaultdict

app = Flask(__name__)

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

# Load orders and count them
order_count_by_user = defaultdict(int)
with open('orders.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user_id = int(row["user_id"])
        order_count_by_user[user_id] += 1

# Merge user with order count
for user in users:
    user["order_count"] = order_count_by_user.get(user["id"], 0)

@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
