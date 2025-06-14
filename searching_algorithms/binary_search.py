"""
Binary Search:- Begin at the middle of the the ordered Array List. -> If the the middle element matches the target, return the index of the matched element. -> Else, if the middle element is greater than the target, remove all the the elements from the middle element to the last element and repeat step one. -> Else, if middle element is less than the target, remove all the elements from the first element to the middle element and reapeat step one untl. -> Else, return target not found

"""

#--------------------------------Binary Search function------------------------------

def binary_search(list, target):
    first = 0
    last = len(list) -1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
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
result = binary_search(my_list, 6)
verify(result)
            
