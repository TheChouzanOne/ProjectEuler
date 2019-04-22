import numpy as np
from time import time 
t=time()

ans = sum(int(x) for x in str(np.math.factorial(100)))

print(ans)
print("Time: %s"%(time()-t))