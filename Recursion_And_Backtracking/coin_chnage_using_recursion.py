# The main goal of this function is to return the coin change for the given amounnt
# if coins are [1,2,5] and the target is 5 change would be 5=[1,1,1,1,1],[1,1,1,2],[1,2,2],[5]]

def coin_change(coins,target):
    if len(coins) == 0 or target < 0:
        return
    coin_change_helper(coins,target)

def coin_change_helper(coins,target,start_index=0,buffer=[],sum=0):
    if sum > target:
        return
    if sum == target:
        print(buffer)
        return
    
    i = start_index
    while( i < len(coins)):
        buffer.append(coins[i])
        coin_change_helper(coins,target,i,buffer,sum+coins[i])
        buffer=[]
        i += 1

#main
coin_change([1,2,5],5)
    