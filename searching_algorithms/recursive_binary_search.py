"""
Recursion simply means a function calling itself a number of times
"""

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:  # Compare the value at the midpoint
            return True
        else:
            if list[midpoint] > target:  # Search in the left half
                return recursive_binary_search(list[:midpoint], target)
            else:  # Search in the right half (exclude the midpoint)
                return recursive_binary_search(list[midpoint + 1:], target)

def verify(index):
    print('target found?:', index)
    if index is not False:
        print('Great! You made it')
    else:
        print('Ooooops!!!')

# ----------------Create a list---------------------
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ---------------Calling the functions and testing the Algorithm-------------------------------
result = recursive_binary_search(my_list, 5)
verify(result)