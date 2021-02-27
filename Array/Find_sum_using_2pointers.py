# The main goal of this function is to find x which is the sum of two numbers in an array
# [1,2,3,4,6] output should be index 1 and index because their sum is 8
# The function takes argument as array and x

def find_sum(lst,x):
    start = 0
    end = len(lst) - 1
    while (start < end):
        sum = lst[start] + lst[end]
        if sum < x:
            start += 1
        elif sum > x:
            end -= 1
        else:
            return (lst[start],lst[end])
    return None

test_arr = [1,2,3,5,6,7]
x = 11
y = find_sum(test_arr,x)
print(y[0],y[1])