# The main goal of this function is to find the closest number to the taget
# for example if lst= [2,5,6,7,8,9], target = 4, output = 5
# The function takes argument as an array and target

def find_closest_number(lst,target):
    min_dif = float('inf')
    start = 0 
    end = len(lst) - 1
    closest_num = None

    if (len(lst) == 0):
        return None
    if len(lst) == 1:
        return lst[0]

    while start <= end:
        mid = (start + end) // 2
        if mid + 1 < len(lst):
            right_diff = abs(lst[mid + 1] - target)
        
        if mid > 0:
            left_diff = abs(lst[mid - 1] - target)
        
        if left_diff < min_dif:
            min_dif = left_diff
            closest_num = lst[mid - 1]
        
        if right_diff < min_dif:
            min_dif = right_diff
            closest_num = lst[mid + 1]
        
        if lst[mid] > target:
            end = mid - 1

        elif lst[mid] < target:
            start = mid + 1
        else:
            return lst[mid]
    print(closest_num)
    return closest_num

# main
lst = [1,2,4,5,7,8,9]
target = 6
find_closest_number(lst,target)

        
