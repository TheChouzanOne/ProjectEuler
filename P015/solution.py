from time import time
t=time()

ans = 1
for i in range(21,41):
    ans *= i
for i in range(1,21):
    ans /= i

print(ans)
print("Time: %s"%(time()-t))