# The main goal of this function is to find the index for a new number
# A = [1,2,4,5,6,8] and t = 3 return index = 2
# The function takes argument as array and and target

def find_proper_index(lst,target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = start + end // 2
        if lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
        else:
            return mid

    print(start)
    return start

lst = [1,2,4,5,6,8]
find_proper_index(lst,0)