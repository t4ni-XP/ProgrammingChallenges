import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append([int(num) for num in input() if num.isdigit()])

# print(grid)
    
q = deque()
visited = [[False] * m for _ in range(n)]

q.append([0, 0, 0]) #x,y,移動回数
visited[0][0] = True
flag = 0

while q:
    direction = [(-1,0), (0,-1), (1,0), (0,1)]
    x, y, count = q.popleft()
    if x == n-1 and y == m-1:
        print(count)
        flag = 1
        break
    number = grid[x][y]

    for dx,dy in direction:
        nx = x + number * dx
        ny = y + number * dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append([nx, ny, count + 1])


if flag == 0:
    print(-1)


# print(visited)