"""
Sorts a list in ascending order and returns a new sorted list.

#---------Steps-----------

Divide: Find the midponit of the list and divide it into sublists.
Conquer: Recursively sort the sublists created in previous step
Combine: Merge the sorted sublists created in previous step

"""

from time import time #To know the time it took to complete the tast, the `time()` library is used


def merge_sort(list):
    if len(list) <= 1:
        return list
    else:
        left_half, right_half = split(list)
        left = merge_sort(left_half)
        right = merge_sort(right_half)

        return merge(left, right)

def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l


"""
To know the time it took to complete the tast, the `time()` library is used
"""


start_time = time()  #To know the start time of the operation

my_list = [5,654,76,567,54,677,33,2,1,4566,44,32,567,332,98]

result = merge_sort(my_list)
print(result)

print("=================")

duration = time() - start_time # To check the duration
print("It took", duration, "Sec. to complete the task")