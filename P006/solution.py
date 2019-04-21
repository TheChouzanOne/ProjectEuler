from time import time
t0 = time()
N = 100

gauss = lambda x: x*(x+1)/2

ans = gauss(N)*(gauss(N)-((2*N+1)/3))

print(ans)
print("Time: %s"%(time()-t0))