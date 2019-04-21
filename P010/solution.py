from time import time

t0 = time()
N = 2000000

def sieve(N):
    nums = list()
    nums.append(False)
    nums.append(False)
    for i in range(2, N):
        nums.append(True)

    for n in range(2, len(nums)):
        if nums[n]:
            for m in range(n+n, len(nums), n):
                nums[m] = False
            yield n
ans = 0
for prime in sieve(N):
    ans+=prime

print(ans)
print("Time: %s"%(time()-t0))