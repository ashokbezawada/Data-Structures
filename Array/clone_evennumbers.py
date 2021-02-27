# The main goal of this function is to clone even numbers for example:
# lst = [1,2,6,0], output should be [1,2,2,6,6,0,0]
# note no extra array should be created for the output, assume array has the space to clone all the numbers
# Present in intial array
# The function takes argument as list

def clone_evenNumbers(lst):
    if lst is None:
        return None
    end = len(lst)
    i = findlastnum(lst)
    print(i)
    while(i >= 0):
        if (lst[i] % 2 == 0):
            end -= 1
            lst[end] = lst[i]
            end -= 1
            lst[end] = lst[i]
        else:
            end -= 1
            lst[end] = lst[i]
        
        i -= 1

    print(lst)

# The main goal of this function is to find the last number present in the list
def findlastnum(arr):
    if arr is None:
        return
    for i in arr:
        if i is not None:
            temp = i
    return arr.index(temp)


# Main
sample_arr = [2,4,1,0,3,None,None,None]
clone_evenNumbers(sample_arr)