import sys
# the main goal of this function is to find the subarray to be sorted 
# for example [1,3,5,2,6,4,7,8,9] ---> [3,5,2,6,4]
# The function takes argument as an array and return the sub array 

def find_subarray_tobe_sorted(lst):
    for start in range(len(lst) - 1):
        if (lst[start+1] < lst[start]):
            break

    if start == len(lst) - 1:
        return None
    
    for end in range(len(lst)-1,0,-1):
        if lst[end-1] > lst[end]:
            break
    
    # find max and min
    max = -(sys.maxsize - 1)
    min = sys.maxsize

    for k in range(start,end):
        if(lst[k] > max):
            max = lst[k]
        if (lst[k] < min):
            min = lst[k]
    
    while(start > 0 and lst[start - 1] > min):
        start -= 1
    
    while(end < len(lst) - 1 and lst[end + 1] < max):
        end += 1
    
    print(start,end)


# main
sample_lst = [1,3,5,2,6,4,7,8,9]
find_subarray_tobe_sorted(sample_lst)