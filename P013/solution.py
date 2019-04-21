from time import time
t = time()

with open('number.txt') as f:
    text = f.read().split('\n')
    numbers = [int(x) for x in text]

ans = sum(numbers)

while (ans > 9999999999):
    ans //= 10

print(ans)
print("Time: %s"%(time()-t))