# The main goal of this function is to find longest increasing subsequence
# The function takes argument as a sequence

def findlongestIncresingSubsequence(sequence):
    n = len(sequence)
    result_arr = [1]*(n)

    for i in range(1,n):
        for j in range(0,i):
            if sequence[i] > sequence[j] and result_arr[i] < result_arr[j] + 1:
                result_arr[i] = result_arr[j] + 1
    
    maximum = 0
    for i in range(n):
        if result_arr[i] > maximum:
            maximum = result_arr[i]
    
    print(maximum)
    return maximum

sequence = [10, 22, 9, 33, 21, 50, 41, 60]
findlongestIncresingSubsequence(sequence)


