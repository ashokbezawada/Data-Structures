#The main goal of this function is to print all the subsests of the array

def print_allsubsets(main_arr,buffer,start_index,buffer_index):
    print(buffer[0:buffer_index])
    if buffer_index == len(buffer):
        return
    if start_index == len(main_arr):
        return
    i = start_index
    while(i < len(main_arr)):
        buffer[buffer_index] = main_arr[i]
        print_allsubsets(main_arr,buffer,i+1,buffer_index+1)
        i += 1

main_arr = [1,2,3]
buff = [None,None,None]
print_allsubsets(main_arr,buff,0,0)

