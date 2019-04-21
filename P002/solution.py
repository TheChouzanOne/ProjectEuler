from time import time
t0 = time()
a=1
b=2
ans = 2

while(b<4000000):
    nextN = a+b
    a = b
    b = nextN
    if(b%2==0):
        ans+=b
print(ans)
print("Time: ",time()-t0)