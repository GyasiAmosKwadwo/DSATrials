"""
Algorithm.

1. Search for a given value in a given array by sequential search
2. Input an array A[0..n-1] and a search key K
3. Output The Index of the first element of A that matches K // -1 if there arer no matching elements

"""
def sequential_search(list, target):
    
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
#----------------Function to verify results----------------------
def verify(index):
    if index is not None:
        print('target found at index:', index)
    else:
        print('target not found in the list')


#----------------Create a list---------------------
my_list = [1,2,3,4,5,6,7,8,9,10, 234,453, 34544,342342, 234,23,234,43,2,3210,10]

#---------------Calling the functions and testing the Algorithm-------------------------------
result = sequential_search(my_list, 10)
verify(result)

    

