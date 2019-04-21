from time import time
from numpy import lcm
from functools import reduce
t0 = time()
N = 20

ans =reduce(lcm, range(1,N+1), 1)

print(ans)
print("Time: %s"%(time()-t0))