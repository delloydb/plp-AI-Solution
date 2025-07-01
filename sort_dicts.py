"""
Filename: sort_dicts.py
Description: Contains two functions to sort a list of dictionaries by a given key:
1. Manual implementation using insertion logic.
2. Efficient implementation using Python's built-in sorted() function.
"""

# Manual implementation
def sort_dicts_manual(dict_list, key):
    """
    Sorts a list of dictionaries manually by a specified key using insertion logic.
    
    Args:
        dict_list (list): List of dictionaries to sort.
        key (str): Key to sort by.

    Returns:
        list: Sorted list of dictionaries.
    """
    sorted_list = []
    for item in dict_list:
        inserted = False
        for i in range(len(sorted_list)):
            if item[key] < sorted_list[i][key]:
                sorted_list.insert(i, item)
                inserted = True
                break
        if not inserted:
            sorted_list.append(item)
    return sorted_list


# AI-suggested (efficient) implementation
def sort_dicts_efficient(dict_list, key):
    """
    Sorts a list of dictionaries using Python's built-in sorted() and lambda.

    Args:
        dict_list (list): List of dictionaries to sort.
        key (str): Key to sort by.

    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda x: x[key])


# Example usage
if __name__ == "__main__":
    data = [
        {"name": "Mango", "price": 30},
        {"name": "Banana", "price": 10},
        {"name": "Apple", "price": 20}
    ]

    print("Original List:")
    print(data)

    print("\nSorted (Manual):")
    print(sort_dicts_manual(data, "price"))

    print("\nSorted (Efficient):")
    print(sort_dicts_efficient(data, "price"))
