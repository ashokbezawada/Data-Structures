# The main goal of this function is to find the prefix sum
# for example if prefix sum = 0, lst = [-1,2,1,-4,2,3,-1,2] return (0,4)
# The function takes argument as array and returns a 1 pair of indexes

def find_prefix_sum(lst):
    map = {}
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
        if sum == 0:
            return (0,i)
        if sum in map:
            new = find_index(map,sum)
            return(new,i)
        map[i] = sum

def find_index(map,sum):
    keys = list(map.keys())
    start = keys.index(sum)
    return start + 1

lst = [-1,2,1,-4,2,3,-1,2]
find_prefix_sum(lst)    
