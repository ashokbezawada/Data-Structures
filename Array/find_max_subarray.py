# The main goal of this function is to find the maximum sum array
# The function takes argument as an array in which max sub array to be found

def find_max_subarray(lst):
    result = lst[0]
    max_ending_here = lst[0]
    for i in range(1,len(lst)-1):
        max_ending_here = max(lst[i],max_ending_here + lst[i])
        result = max(result,max_ending_here)
    print(result)
    return result


lst = [-2,-3,4,-1,-2,1,5,-1]
find_max_subarray(lst)