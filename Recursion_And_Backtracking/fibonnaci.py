# The main goal of this function is to implement the fibonnaci series using recursion
# The function takes argument as number whose fibbonaci sum has to be found

def fibonnaci(n):
    if n < 0 :
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

print(fibonnaci(9))

# The main goal of this function is to perform fibonnaci using memorization 
# The function takes argument as a number 

hash_tab = dict()
def fibonnaci_using_memorization(n):
    if n < 0:
        return None
    if n in hash_tab:
        return hash_tab[n]
    elif n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibonnaci_using_memorization(n-1) + fibonnaci_using_memorization(n-2)
    
    hash_tab[n] = value
    return value
  
print(fibonnaci_using_memorization(9))
