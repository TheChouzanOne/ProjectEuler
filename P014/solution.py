#THIS IS NOT MY OWN SOLUTION. Comes from stewSquared in PE.
from time import time
t=time()
def collatz(n): return n//2 if n%2==0 else 3*n+1

def distance(n, cache={1:1}):
    if n not in cache: cache[n] = distance(collatz(n))+1
    return cache[n]
ans = max(range(1,1000000), key=distance)
print(ans)
print("Time: %s"%(time()-t))