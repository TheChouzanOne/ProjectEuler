from time import time
t0 = time()
ans = 0
for i in range(1,1000):
    if(i%3==0):
        ans += i
    if(i%5==0):
        ans += i
    if(i%15==0):
        ans -= i
print(ans)
print("Time: %s"%(time()-t0))
