from time import time
t=time()

triangle = list()
with open('triangle.txt') as f:
    lines = f.read().split('\n')
    for line in lines:
        triangle.append( [int(x) for x in line.split(" ")] )

rowMaxIndex = len(triangle)-1

for i in range(rowMaxIndex-1, -1, -1):
    for j in range(i+1):
        print(i,j)
        triangle[i][j] +=  max(triangle[i+1][j], triangle[i+1][j+1])

# for i in triangle:
#     print(i)

ans = triangle[0][0]

print(ans)
print("Time: %s"%(time()-t))