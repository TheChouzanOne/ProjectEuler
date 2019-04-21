from time import time

t0 = time()
adj = 13
zeros = 0
with open('number.txt') as f:
    number = f.read()
ans = 0
new = 1
for i in range(1000):

    if(number[i]=='0'):
        zeros += 1

    new *= max(1, int(number[i]))
    if i >= adj:
        if(number[i-adj]=='0'):
            zeros -= 1
        new /= max(1, int(number[i-adj]))
    if(new > ans and zeros==0):
        ans = new

    
        

print(ans)
print("Time: %s"%(time()-t0))