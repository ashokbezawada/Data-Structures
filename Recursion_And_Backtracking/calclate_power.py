# The main goal of this function is to calculate the power
# The function takes argument as base and power

# albert method 
def pow_albert(x,n):
    if n == 0:
        return 1
    else:
        return x * pow(x,n-1)

# The main goal of this function is to find the power 
# Using the pinto's method the time complexity can be reduced to log(n)
# The function takes argument as base and power

def pow_pinto(x,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = pow_pinto(x,n//2)
        return y * y
    else:
        return x * pow_pinto(x,n-1)

# main 
print(pow_albert(2,8))
print(pow_pinto(-2,8))