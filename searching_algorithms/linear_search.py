"""
Linear search :- Loop through an ordered list and compare each element, one after the other to the target. If the element matches the target, return the index of the matched element, else return target not found

"""


#--------Function to loop through and compare elements with target--------------
def linear_search(list, target):
    
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
my_list = [1,2,3,4,5,6,7,8,9,10]

#---------------Calling the functions and testing the Algorithm-------------------------------
result = linear_search(my_list, 3)
verify(result)
