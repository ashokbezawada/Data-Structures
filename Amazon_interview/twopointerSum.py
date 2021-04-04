# The main goal of this function is to check whether the two points sum exists or not

def find_sum(arr,val):
    visited = set()
    for i in arr:
        if val-i in visited:
            print([i,val-i])
            return True
        visited.add(i)
    return False

find_sum([2, 1, 8, 4, 7, 3],7)