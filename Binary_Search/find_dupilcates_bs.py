# The main goal of this function is to find the first occurence of the target
# for example lst = [1,2,2,5,6] and target = 2, both 1,2 indexes have 2 our function should 
# return first occurence which 1
# The function takes argument as lst and target

def find_first_occurence(lst,target):
    start = 0
    end = len(lst) - 1
    while (start <= end):
        mid = start + (end - start) % 2
        if lst[mid] > target or lst[mid] == target and mid > 0 and lst[mid - 1] == target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
        else:
            print(mid)
            return mid

lst = [1,2,5,6,8,8]
find_first_occurence(lst,8)