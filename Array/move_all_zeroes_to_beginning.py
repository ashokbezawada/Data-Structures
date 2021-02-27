# The main goal of this function is to move all zeroes to the beginning 
# for example : lst [2,4,0,3,0,1,0]
# The function takes argument as an array that has zeroes to be moved front

def moves_zeroes_to_front(lst):
    boundary = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            # Do the swap
            temp = lst[boundary]
            lst[boundary] = lst[i]
            lst[i] = temp
            boundary += 1
    print(lst) 



# main
lst = [2,4,0,3,0,1,0]
moves_zeroes_to_front(lst)