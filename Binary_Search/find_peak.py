# the main goal of this function is to find the peak element
# for example lst =[1,3,4,5,2] peak = 5 and lst = [5,3,1] peak = 5
# The function takes argument as lst 

def find_peak(lst):
    start = 0 
    end = len(lst) - 1
    # base condition 
    if len(lst) < 3:
        return None
    while(start <= end):
        mid = (start + end)//2
        left_mid = lst[mid - 1] if lst[mid - 1] > 0 else float("-inf")
        right_mid = lst[mid + 1] if lst[mid + 1] < len(lst) else float("inf")
        # conditions
        if left_mid < lst[mid] and right_mid > lst[mid]:
            start = mid + 1
        elif left_mid > lst[mid] and right_mid < lst[mid]:
            end = mid - 1
        elif left_mid < lst[mid] and right_mid < lst[mid]:
            print(lst[mid])
            return lst[mid]
    return None

lst =[[1,2,3,4,5,4,3,2,1],[1,2,3,4,1],[1,6,5,4,3,2,1]]
for i in lst:
    find_peak(i) 
