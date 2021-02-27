# The main goal of this function is to implement the binary search
# The function takes arguments as an array and target integer

def binary_search(lst,target):
    start = 0
    end = len(lst) - 1
    while(start <= end):
        middle = start + (end - start)%2
        if lst[middle] > target:
            end = middle - 1
        elif lst[middle] < target:
            start = middle + 1
        else:
            print("The target found at index" ,middle)
            return middle
    return None


# main
sample_lst = [1,2,4,7,9]
binary_search(sample_lst,2)