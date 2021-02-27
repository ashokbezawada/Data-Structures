# The main goal of this function is to reverse an array by using two pointers
# The function takes argument as an array that has to be reversed 

def reverse_arr(lst):
    start = 0
    end = len(lst) - 1
    while (start < end):
        temp = lst[start]
        lst[start] = lst[end]
        lst[end] = temp
        start += 1
        end -= 1
    print(lst)
    return lst

# main
lst = [1,2,3,4,5]
reverse_arr(lst)
