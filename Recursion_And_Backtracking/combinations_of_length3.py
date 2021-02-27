# The main goal of this function is to print all the combinationss of  length 3
from itertools import combinations
def print_combos(arr,buffer,start_index,buffer_index):
    if buffer_index == len(buffer):
        print(buffer)
        #buffer = []
        return
    if start_index == len(arr):
        return
    i = start_index
    while(i<len(arr)):
        buffer[buffer_index] = arr[i]
        print_combos(arr,buffer,i+1,buffer_index+1)
        i += 1

arr = [1,2,3,4,5]
buffer = [None,None,None]
print_combos(arr,buffer,0,0)

comb_lst = list(combinations(arr,3))
print(comb_lst)




    