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
    size = len(values)
    coins = values
    DPtable = [ [0] * size for i in range(amount + 1) ]
    DPtable[1][0] = 1
    
    #amount = 0 means we didn't use any coins
    if amount == 0:
        return [coins, 0]
    #amount = smallest value means we just use one of the smallest coin
    elif amount == values[0]:
        coins[0] += 1
        return [coins, 1]
    #calculate values for DPtable in bottom-up fashion
    else:
        #create array with incremented values up to amount so the default value
        #is with using all 1 cent coins
        sums = range(amount+1)

        for i in range(amount+1):
            for j in range(size):
            
                # if i plus this coin (j)'s value is greater than amount, break
                # otherwise, if sums [at i plus this coin's value] greater than sums[i]+1
                # so if number at sums we can reach next with current coin holds a worse 
                # solution than adding one coin to sums[i], then we need to update the
                # table with the better solution.
                # so table[i+coin value] = table[i] <--entire row
                # and table[i+coin value][j = current coin] += 1
                # and sums [at i plus this coin's value] = sums[i]+1

                if (i + coins[j])  > amount:
                    break
                elif (sums[i + coins[j]]) >= (sums[i]+1):
                    DPtable[i + coins[j]] = DPtable[i][:]
                    DPtable[i + coins[j]][j] += 1
                    sums[i + coins[j]] = sums[i] + 1
                    
    # finally, return array at DPtable[amount] for coin numbers and sum[amount]
    # for number of coins used                
    return [DPtable[amount], sums[amount]]



