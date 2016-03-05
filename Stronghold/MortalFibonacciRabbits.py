def mortalrabbits(month, deathrate):
    if(month <= 1):
        return 1
    elif(month <=deathrate-1):
        if month-1 not in memoize:
            memoize[month-1] = mortalrabbits(month-1, deathrate)
        if month-2 not in memoize:
            memoize[month-2] = mortalrabbits(month-2, deathrate)            
        return memoize[month-1]+memoize[month-2]
    else:
        print month
        bunnies = 0
        for i in range(deathrate-1, month-2):
            if i not in memoize:
                memoize[i] = mortalrabbits(i, deathrate)
            bunnies+=memoize[i]
        return bunnies
    
    
file = open("C:\\Users\\Aaron\\Downloads\\rosalind_fibd (1).txt","r").readline().split(" ")
n = int(file[0])
m = int(file[1])
memoize = dict()
a = mortalrabbits(n,m)
print a
