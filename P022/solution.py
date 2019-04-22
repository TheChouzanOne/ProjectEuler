from time import time
import numpy as np
t=time()

def score(word):
    c = 0
    for char in word:
        if(char=='"'):
            continue
        c += ord(char)-ord('A')+1
    return c

with open('names.txt') as f:
    names = f.read().split(',')

names = sorted(names)

names = map(score, names)
c = 1
ans = 0
for name in names:
    ans += c * name
    c+=1

print(ans)
print("Time: %s"%(time()-t))