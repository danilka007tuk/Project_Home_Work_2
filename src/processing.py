from typing import Dict, List, Any


def filter_by_state(last_dict: List[Dict], value_key: str = "EXECUTED") -> List[Dict]:
    """Ф"""
    new_list_dict = []
    for every_dict in last_dict:
        if every_dict["state"] == value_key:
            new_list_dict.append(every_dict)
    return new_list_dict


def sort_by_date(list_dict: List[Dict], arg_for_sort: bool = True) -> List[Dict]:
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict["date"], reverse=arg_for_sort)
    return sort_list
