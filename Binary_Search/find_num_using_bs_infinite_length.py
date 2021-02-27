# The main goal of this function is to find the number in array using binary search where the length of array is unknown
# The function takes arguments as target and array 

def find_ind_infinite_length(lst,target):
    ind = exp = 0
    while True:
        try:
            if lst[ind] == target:
                return ind
            elif lst[ind] < target:
                ind = 2**exp
                exp += 1
            else:
                break
        except IndexError:
            break
    
    start = ind//2 + 1
    end = ind - 1
    while(start <= end): 
        try :
            mid = (start + end)//2
            if lst[mid] == target:
                return mid
            elif lst[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        except IndexError:
            end = mid - 1
    return None

arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170] 
target_ind = find_ind_infinite_length(arr,170)
print(arr[target_ind])
    