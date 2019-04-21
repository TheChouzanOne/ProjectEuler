from time import time
import numpy as np

t = time()
N = 500

def nDivisors(n):
    divs = 0
    for i in range (1,int(np.sqrt(n))+1):
        if(n%i==0):
            if(n/i==i):
                divs += 1
            else:
                divs += 2
    return divs


divs = 0
n = 0
while(divs <= 500):
    n+=1
    ans = n*(n+1)/2
    if(n%2==1):
        divs = nDivisors((n+1)/2) * nDivisors(n)
    else:
        divs = nDivisors(n/2) * nDivisors(n+1)
print(ans)
print("Time %s"%(time()-t))