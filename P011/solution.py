from time import time

t0 = time()
N = 20
adj = 4
adj -= 1
grid = list()
with open('numbers.txt') as f:
    for i in range(20):
        grid.append([int(x) for x in f.readline().split(" ")])

ans = 0

for i in range(N):
    for j in range(adj,N):
        num = grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3]
        if num > ans:
            ans = num

for i in range(adj,N):
    for j in range(N):
        num = grid[i][j] * grid[i-1][j] * grid[i-2][j] * grid[i-3][j]
        if num > ans:
            ans = num

for i in range(adj,N):
    for j in range(adj,N):
        num = grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3]
        if num > ans:
            ans = num

for i in range(adj,N):
    for j in range(N-adj):
        num = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
        if num > ans:
            ans = num

print(ans)
print("Time: %s"%(time()-t0))