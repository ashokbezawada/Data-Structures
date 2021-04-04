# The main goal of this function is to implement fibonnaci using dynamic programming
# The function takes argument as number whose fibonnaci series to find out

def fibonnaci(x):
    arr = []
    arr.append(1)
    arr.append(1)
    start = 2
    while start <= x:
        fib = arr[start-1] + arr[start-2]
        arr.append(fib)
        start += 1
    # the value of x is
    print("the value of x is : ",arr[x-1])


# main 
fibonnaci(5)


