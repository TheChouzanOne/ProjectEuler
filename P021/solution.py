from time import time
import numpy as np
t=time()
N=10000
def divisorsSum(n):
    c = 0
    for i in range (1,int(np.sqrt(n))+1):
        if(n%i==0):
            if(n/i==i):
                c += i
            else:
                c += i + n/i
    return c-n #I need divisors LESS THAN n

ans=0

for i in range(2,N):
    b = divisorsSum(i)
    if(b < N and b!=i and i == divisorsSum(b)):
        ans += i+b

ans /= 2

print(ans)
print("Time: %s"%(time()-t))