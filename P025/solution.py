from time import time
t = time()

def digits(x):
    return len(str(x))
N=1000
a=1
b=1
ans = 2
while(digits(b)!=N):
    ans += 1
    nextN = a+b
    a = b
    b = nextN
print(ans)
print("Time: ",time()-t)