# The main goal of this function is to find missing number in array or not
def findMissingnumber(lst):
    initial_sum = total_sum = 0
    for i in lst:
        initial_sum = initial_sum + i
    
    for j in range(len(lst)+2):
        total_sum = total_sum + j
    result = total_sum - initial_sum
    print(result)
    return result

# main 
findMissingnumber([3, 7, 1, 2, 8, 4, 5])
