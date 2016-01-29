"""
Three Coin Change Functions
Parameters:
    An array of cpins values in ascending order, the first is = 1
    An integer value for Change
Return Value:
    Results[ [array of coins], number of coins]
"""
#Slow Change
def slowChange(values, amount):
    results = [values, amount]
    return results

#Greedy
def greedy(values, amount):
    size = len(values)
    coins = [0]*size
    used = 0
    #create an iterator, vn...0
    for i in range(size-1, -1, -1):
        while amount >= values[i]:
            amount = amount - values[i]
            used = used + 1
            coins[i] = coins[i] + 1
        if amount == 0:
            break
    return [coins, used]
    
#Dynamic
def dynamic(values, amount):
    results = [values, amount]
    return results



