from time import time
import numpy as np
from functools import reduce
t0 = time()
N = 20

ans =reduce(np.lcm, range(1,N+1), 1)

print(ans)
print("Time: %s"%(time()-t0))