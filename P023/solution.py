from time import time
import numpy as np
t=time()
N=28123
def divisorsSum(n):
    c = 0
    for i in range (1,int(np.sqrt(n))+1):
        if(n%i==0):
            if(n/i==i):
                c += i
            else:
                c += i + n/i
    return c-n #I need divisors LESS THAN n

abundantN = [x for x in range(1,N+1) if divisorsSum(x) > x]

writable = list()
for i in range(N+1):
    writable.append(False)
for i in range(len(abundantN)):
    for j in range(i, len(abundantN)):
        ab = abundantN[i] + abundantN[j]
        if ab <= N:
            writable[ab] = True

sumWriteable = 0
for i in range(N+1):
    if writable[i]:
        sumWriteable += i

ans = (N)*(N+1)/2 - sumWriteable

print(ans)
print("Time: %s"%(time()-t))