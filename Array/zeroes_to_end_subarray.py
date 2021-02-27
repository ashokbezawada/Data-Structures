# The main goal of this function is to move all zeroes to the end of the sub array
# for example lst = [0,4,0,1,2,0,3]  output should be [4,1,2,3,0,0,0]
# The function takes argument as an array that has to be moved

def move_zeroes_to_end(lst):
    boundary = len(lst) - 1
    for i in range(len(lst)-1,-1,-1):
        if lst[i] == 0:
            temp = lst[boundary]
            lst[boundary] = lst[i]
            lst[i] = temp
            boundary -= 1
    print(lst)


# main
lst = [0,4,0,1,2,0,3]
move_zeroes_to_end(lst)