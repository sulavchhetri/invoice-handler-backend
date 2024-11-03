import requests
import json


url = "http://127.0.0.1:8000/invoices/"
# # res = requests.post(url, json=data)

# res = requests.get(url)

# with open("r.json", "w") as file:
#     json.dump(res.json(), file)


# res = requests.delete("http://127.0.0.1:8000/invoices/6.1.1")

# data = {
#     "hours": 10,
#     "task_id":"6.1.1",
#     "amount":500,
#     "discount": 10,
#     "unit_price": 50,
#     "task": "Task 6.1.1"
# }


data = {
    "1": {
        "task": "Task 1",
        "hours": 40,
        "unit_price": 150,
        "discount": 20,
        "amount": 3000,
        "task_id": "1",
        "1.1": {
            "task": "Task 1.1",
            "hours": 60,
            "unit_price": 20,
            "discount": 10,
            "amount": 2000,
            "task_id": "1.1",
        },
        "1.2": {
            "task": "Task 1.2",
            "hours": 120,
            "unit_price": 30,
            "discount": 50,
            "amount": 1000,
            "task_id": "1.2",
        },
    },
    "2": {
        "task": "Task 2",
        "hours": 30,
        "unit_price": 300,
        "discount": 25,
        "amount": 500,
        "task_id": "2",
    },
    "3": {
        "task": "Task 3",
        "hours": 100,
        "unit_price": 25,
        "discount": 15,
        "amount": 100,
        "task_id": "3",
    },
    "4": {
        "task": "Task 4",
        "hours": 8,
        "unit_price": 600,
        "discount": 1000,
        "amount": 1500,
        "task_id": "4",
    },
    "5": {
        "task": "Task 5",
        "hours": 100,
        "unit_price": 500,
        "discount": 2500,
        "amount": 2000,
        "task_id": "5",
    },
    "6": {
        "task": "Task 6",
        "hours": 60,
        "unit_price": 150,
        "discount": 300,
        "amount": 3000,
        "task_id": "6",
        "6.1": {
            "task": "Task 6.1",
            "hours": 70,
            "unit_price": 150,
            "discount": 300,
            "amount": 2000,
            "task_id": "6.1",
            "6.1.1": {
                "task": "Task 6.1.1",
                "hours": 50,
                "unit_price": 150,
                "discount": 200,
                "amount": 1000,
                "task_id": "6.1.1",
            },
        },
    },
}


res = requests.post("http://127.0.0.1:8000/invoices/", json=data)


print(res.status_code, res.json())
