# The main goal of this function is to generate all the substrings
# The function takes arguments as two strings and generate its substrings

def generate_sub_strings(x,y):
    # listx to store all the substrings of x
    # list y to store all the substrings of y
    listx = [x[i: j] for i in range(len(x)) 
          for j in range(i + 1, len(x) + 1)]
    
    listy = [y[i: j] for i in range(len(y)) 
           for j in range(i + 1, len(y) + 1)]
    
    return listx,listy

# The main goal of this function is find the longest common substring from strings that are present in the two lists
# The function takes arguments as two lists
def find_longest_common_substring(lst1,lst2):
    final_arr = []
    for i in lst1:
        for j in lst2:
            if i == j:
                final_arr.append(i)
    max = 0
    longest_common_substring = ""
    for i in final_arr:
        x = len(i)
        if x > max:
            max = x
            longest_common_substring = i
    print(longest_common_substring)




z = generate_sub_strings("ab","abc")
find_longest_common_substring(z[0],z[1])