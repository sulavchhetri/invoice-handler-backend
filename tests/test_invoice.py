from collections import defaultdict
import json

invoices = [
    {
        "hours": 40,
        "discount": 20,
        "task": "Task 1",
        "unitprice": 150,
        "task_id": "1",
        "amount": 3000
    },
    {
        "hours": 60,
        "discount": 10,
        "task": "Task 1.1",
        "unitprice": 20,
        "task_id": "1.1",
        "amount": 2000
    },
    {
        "hours": 120,
        "discount": 50,
        "task": "Task 1.2",
        "unitprice": 30,
        "task_id": "1.2",
        "amount": 1000
    },
    {
        "hours": 30,
        "discount": 25,
        "task": "Task 2",
        "unitprice": 300,
        "task_id": "2",
        "amount": 500
    },
    {
        "hours": 100,
        "discount": 15,
        "task": "Task 3",
        "unitprice": 25,
        "task_id": "3",
        "amount": 100
    },
    {
        "hours": 8,
        "discount": 1000,
        "task": "Task 4",
        "unitprice": 600,
        "task_id": "4",
        "amount": 1500
    },
    {
        "hours": 100,
        "discount": 2500,
        "task": "Task 5",
        "unitprice": 500,
        "task_id": "5",
        "amount": 2000
    },
    {
        "hours": 60,
        "discount": 300,
        "task": "Task 6",
        "unitprice": 150,
        "task_id": "6",
        "amount": 3000
    },
    {
        "hours": 70,
        "discount": 300,
        "task": "Task 6.1",
        "unitprice": 150,
        "task_id": "6.1",
        "amount": 2000
    },
    {
        "hours": 50,
        "discount": 200,
        "task": "Task 6.1.1",
        "unitprice": 150,
        "task_id": "6.1.1",
        "amount": 1000
    }
]


def divide_invoices_by_depth(invoices):
    invoices_by_depth = {}
    
    for invoice in invoices:
        task_id = invoice['task_id']
        depth = len(str(task_id).split('.')) - 1
        if depth not in invoices_by_depth:
            invoices_by_depth[depth] = {}
        
        invoices_by_depth[depth][task_id] = invoice
    
    return invoices_by_depth



def get_parent_ids(child_id):
    parts = child_id.split('.')
    parent_ids = []
    
    for i in range(len(parts)):
        parent_ids.append('.'.join(parts[:i + 1]))
    
    return parent_ids[:-1]


def format_invoices(invoices):
    formatted_invoices = {}
    invoices_by_depth = divide_invoices_by_depth(invoices)
    depths = sorted(invoices_by_depth.keys(), key=int)

    for depth in depths:
        if int(depth) == 0:
            formatted_invoices.update(invoices_by_depth[depth])
        else:
            for invoice_id, invoice in invoices_by_depth[depth].items():
                parents = get_parent_ids(invoice_id)
                current_level = formatted_invoices
                
                for index, parent_id in enumerate(parents):
                    if parent_id not in current_level:
                        current_level[parent_id] = {}
                    
                    if index == len(parents) - 1:
                        current_level[parent_id][invoice_id] = invoice
                    else:
                        current_level = current_level[parent_id]

    return formatted_invoices



with open("result.json",'w') as file:
    json.dump(format_invoices(invoices), file)