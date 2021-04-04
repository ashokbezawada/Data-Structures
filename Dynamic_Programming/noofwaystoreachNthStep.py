# The main goal of this function is to find the no.of ways to reach to nth step
# The function takes arguments as steps and nthstep

def findnumberofWays(step_array,n):
    result_array = [0]*(n+1)
    #print(result_array)
    result_array[0] = 1
    start = 0
    while(start <= n):
        for i in step_array:
            #print(start + i)
            if (start + i) < len(result_array):
                result_array[start + i] = result_array[start + i] + result_array[start] 
        start += 1
    print(result_array[n])


# main 
arr = [1,3,5]
n = 8
findnumberofWays(arr,n)