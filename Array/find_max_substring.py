# The main goal of this function is to find the length of maximum substring
# example s = "whatwhywhere" output =atwhy"
# The function takes argument as string

def find_max_substring(s):
    map = {}
    max_length = start = 0
    for i in range(len(s)):
        if s[i] in map and start <= map[s[i]]:
            start = map[s[i]] + 1
        else:
            max_length = max(max_length,i-start+1)
        
        map[s[i]] = i
    return max_length
# main
s ="whatwhywhere"
find_max_substring(s)
