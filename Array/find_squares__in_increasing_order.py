# The main goal of this function is to find squares in increasing order 
# example input = [-4,-2,-1,0,3,5] output = [0,1,4,9,16,25]
# The function takes array as an argument

def find_squares_in_increasing_order(arr):
    end = len(arr) - 1
    start = 0
    new_arr = [None] * len(arr)
    new_index = end
    while(start <= end):
        x = arr[start] * arr[start]
        y = arr[end] * arr[end]
        if x > y:
            new_arr[new_index] = x
            start += 1
        else:
            new_arr[new_index] = y
            end -= 1
        
        new_index -= 1
    print(new_arr)
      

# main
lst = [-4,-2,-1,0,3,5]
find_squares_in_increasing_order(lst)


