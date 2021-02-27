# The main goal of this function is to reverse all characters present in a string
# input = "i live in a house" output = "house a in live i"
# The function takes argument as str and return changed str

def reverse_string(str):
    s = str.split(' ')
    end = len(s) - 1
    i = 0
    new_str = ""
    while(i != end):
        temp = s[end]
        s[end] = s[i]
        s[i] = temp
        end -= 1
        i += 1
    new_str = " ".join(s)
    print(new_str)





# main
reverse_string("i live in a house")



