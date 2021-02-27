# The main goal of this function is to implement the dutch national flag
# example array = [5,2,4,4,6,4,4,3] pivot = 4 and result = [3,2,4,4,4,4,5,6]
# The function takes argument as lst that has to be sorted and takes the pivot element

def dutch_national_flag(lst,pivot):
    low_boundary = 0
    high_boundary = len(lst) - 1
    i = 0
    while(i <=  high_boundary):
        if (lst[i] < pivot):
            lst[low_boundary],lst[i] = lst[i],lst[low_boundary]
            low_boundary += 1
            i += 1
        
        elif (lst[i] > pivot):
            lst[high_boundary],lst[i] = lst[i],lst[high_boundary]
            high_boundary -= 1

        else:
            i += 1 
    
    print(lst)


# main
sample_lst = [5,2,4,4,6,4,4,3]
pivot = 4
dutch_national_flag(sample_lst,pivot)
