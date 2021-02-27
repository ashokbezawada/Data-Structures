# The main goal of this function is to find minimum in cyclic sorted array
# example = [1,2,4,7,8] cyclic rotated by 7 means [7,8,1,2,3] and min is 1
# THe function takes argument as cyclic sorted array

def find_min_cyclic_array(lst):
    start = 0 
    end = len(lst) - 1
    right = lst[end]
    while (start <= end):
        mid = start + end // 2
        if (lst[mid] <= right and (mid == 0 or lst[mid - 1] > lst[mid])):
            print(lst[mid])
            return mid
        elif lst[mid] > right:
            start = mid + 1
        else:
            end = mid - 1
    return None

lst = [7,8,1,2,4]
find_min_cyclic_array(lst)