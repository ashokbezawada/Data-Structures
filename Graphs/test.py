
def reverse_lst(lst):
    length = len(lst) - 1
    end = length
    for i in range(length):
        if i > end:
            break
        else:
            temp = lst[i]
            lst[i] = lst[end]
            lst[end] = temp
            end -= 1
    print(lst) 

#main
lst = [1,2,3,4,5]
reverse_lst(lst)