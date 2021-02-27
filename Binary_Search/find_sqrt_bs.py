# The main goal of this function is to find the square root of the number using binary search
# example square root of 9 = 3 and square root of 5 and 8 is 2
# The function takes a number whose sqaure root to be found

def find_sqrt_bs(x):
    start = 0
    end = x 
    while(start <= end):
        mid = (start + end) // 2
        square_mid = mid * mid
        if square_mid >= x:
            end = mid - 1
        else:
            start = mid + 1
    print(start - 1)
    return start - 1

#main
find_sqrt_bs(8)