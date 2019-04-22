from time import time
t=time()

N = 2**1000
ans = 0
s = str(N)
for i in s:
    ans += int(i)

print(ans)
print("Time: %s"%(time()-t))