# The main goal of this function is to find the max sub array using sliding window technique
# example lst [5,3,1,7,6,4,2,3] target = 14 subarray = [1,7,6]
# The function takes arguments as array and target

def find_subarray(lst,target):
    start = end = 0
    sum = lst[0]

    while start < len(lst):
        if start > end:
            end = start 
            sum = lst[start]
        
        if (sum < target):
            if (end == len(lst) - 1):
                break
            
            end += 1
            sum += lst[end]
        
        elif (sum > target):
            sum -= lst[start]
            start += 1
        
        else:
            print(start,end)
            return(start,end)
    return None

# main
example_lst = [5,3,1,7,6,4,2,3]
find_subarray(example_lst,14)


