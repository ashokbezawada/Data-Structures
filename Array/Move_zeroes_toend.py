# The main goal of this function is to move a specific number to the end
# for example lst = [2,2,4,4,1,0,0,3] and output should be = [2,2,4,4,1,3,0,0]
# The function takes argument as array

def moves_zeroes_toend(lst):
    end = len(lst)
    i = end - 1

    while(i >= 0):
        if (lst[i] == 0):
            end -= 1
            temp = lst[end]
            lst[end] = lst[i]
            lst[i] = temp
        i -= 1
    print(lst)

# main 
zeroes_arr = [2,2,4,4,0,1,0,3]
moves_zeroes_toend(zeroes_arr)