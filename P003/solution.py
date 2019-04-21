from time import time
import numpy as np 
t0 = time()
N = 600851475143

def sieve():
    nums = list()
    nums.append(False)
    nums.append(False)
    for i in range(2, int(np.sqrt(N))):
        nums.append(True)

    for n in range(2, len(nums)):
        if nums[n]:
            for m in range(n+n, len(nums), n):
                nums[m] = False
            yield n
ans = 0
for prime in sieve():
    while(N%prime==0):
        N /= prime
        ans = prime

print(ans)
print("Time: %s"%(time()-t0))