# The main goal of this function is to same colors to adjacent places
# red = o, white = 1, blue = 2, arr= [1,0,1,2,1,0,1,2] output = [0,0,1,1,1,1,2,2]
# The function takes argument as array that has to be sorted and the value of color white

def move_colors_adjacent(lst,col):
    i = 0
    low_boundary = 0
    high_boundary = len(lst) - 1

    while(i <= high_boundary):

        if lst[i] < white:
            lst[low_boundary],lst[i] = lst[i],lst[low_boundary]
            low_boundary += 1
            i += 1
            
        elif lst[i] > white:
            lst[high_boundary],lst[i] = lst[i],lst[high_boundary]
            high_boundary -= 1
        
        else:
            i += 1
    
    print(lst)


# main
test_lst = [1,0,1,2,1,0,1,2]
white = 1
move_colors_adjacent(test_lst,white)