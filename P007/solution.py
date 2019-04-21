from time import time
import math
t0 = time()
N = 10001

def sieve(N):
    nums = list()
    nums.append(False)
    nums.append(False)
    for i in range(2, int(N)):
        nums.append(True)

    for n in range(2, len(nums)):
        if nums[n]:
            for m in range(n+n, len(nums), n):
                nums[m] = False
            yield n
ans = -1
num = 1
for prime in sieve(N*math.sqrt(N)):
    if(num==N):
        ans=prime
        break
    num+=1

print(ans)
print("Time: %s"%(time()-t0))