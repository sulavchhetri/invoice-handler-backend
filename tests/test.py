import requests
import json

data = {
    "1": {
        "task": "Task 1",
        "hours": 40,
        "unit_price": 150,
        "discount": 20,
        "amount": 3000,
        "1.1": {
            "task": "Task 1.1",
            "hours": 60,
            "unit_price": 20,
            "discount": 10,
            "amount": 2000,
        },
        "1.2": {
            "task": "Task 1.2",
            "hours": 120,
            "unit_price": 30,
            "discount": 50,
            "amount": 1000,
        },
    },
    "2": {
        "task": "Task 2",
        "hours": 30,
        "unit_price": 300,
        "discount": 25,
        "amount": 500,
    },
    "3": {
        "task": "Task 3",
        "hours": 100,
        "unit_price": 25,
        "discount": 15,
        "amount": 100,
    },
    "4": {
        "task": "Task 4",
        "hours": 8,
        "unit_price": 600,
        "discount": 1000,
        "amount": 1500,
    },
    "5": {
        "task": "Task 5",
        "hours": 100,
        "unit_price": 500,
        "discount": 2500,
        "amount": 2000,
    },
    "6": {
        "task": "Task 6",
        "hours": 60,
        "unit_price": 150,
        "discount": 300,
        "amount": 3000,
        "6.1": {
            "task": "Task 6.1",
            "hours": 70,
            "unit_price": 150,
            "discount": 300,
            "amount": 2000,
            "6.1.1": {
                "task": "Task 6.1.1",
                "hours": 50,
                "unit_price": 150,
                "discount": 200,
                "amount": 1000,
            },
        },
    },
}


url = "http://127.0.0.1:8000/invoices/"
# res = requests.post(url, json=data)

res = requests.get(url)

print(res.status_code)
print(res.json())


with open("r.json", "w") as file:
    json.dump(res.json(), file)
