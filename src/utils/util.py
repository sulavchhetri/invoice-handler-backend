"""
    This module is used to manipulate invoices
"""

from typing import Dict, List


def get_extra_keys(keys: Dict) -> Dict:
    """
    Filters out the standard keys from the input dictionary
    Args:
        keys (Dict)

    Returns:
        Dict:
    """
    standard_keys_set = ["task", "hours", "unit_price", "discount", "amount"]
    return {key: value for key, value in keys.items() if key not in standard_keys_set}


def divide_invoices_by_depth(invoices: List[Dict]) -> Dict:
    """
    Divides all the flat invoices into layers of depth

    Args:
        invoices (List[Dict])

    Returns:
        Dict
    """
    invoices_by_depth = {}

    for invoice in invoices:
        task_id = invoice["task_id"]
        depth = len(str(task_id).split(".")) - 1
        if depth not in invoices_by_depth:
            invoices_by_depth[depth] = {}

        invoices_by_depth[depth][task_id] = invoice

    return invoices_by_depth


def get_parent_ids(child_id : str) -> List[str]:
    """
    Returns all the parents of the child id
    
    6.1.3.4 --> ['6','6.1','6.1.3']

    Args:
        child_id (str)

    Returns:
        List[str]
    """
    parts = child_id.split(".")
    parent_ids = []

    for i in range(len(parts)):
        parent_ids.append(".".join(parts[: i + 1]))

    return parent_ids[:-1]


def format_invoices(invoices:List[Dict]) -> Dict:
    """
    Returns a tree like invoices from a flatten list of invoices

    Args:
        invoices (List[Dict])

    Returns:
        Dict
    """
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
