def bubble_sort(list):
    temp  = 0
    while len(list) > 1:
        for i in range(0, len(list)):
            for j in range(1, len(list)):
                
                if list[i] > list[j]:
                    temp = list[i]
                    i = list[j]
                    j = temp
        return list




my_list = [23,35,3,24,65,68,65,2,3,5,76,86,34,323,56,86,68,8,65,5,]

results = bubble_sort(my_list)
print(results)
