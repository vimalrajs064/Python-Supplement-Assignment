def add_to_list(item, lst=None):  # Use None instead of []
    if lst is None:
        lst = []                  # Create new list each call
    lst.append(item)
    return lst

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [2]  
print(add_to_list(3))  # [3]
