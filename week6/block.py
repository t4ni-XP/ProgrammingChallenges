import sys
input = sys.stdin.readline
import heapq
from collections import deque

testcases: list[dict] = []
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    block = []
    for _ in range(h):
        block.append([int(num) for num in input() if num.isdigit()])
    testcases.append([h, w, block])

# print(testcases)

for case in testcases:
    h: int = case[0]
    w: int = case[1]
    block: list[int] = case[2]
    directions: list[tuple] = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    dist: list[int] = [[float('inf')] * w for _ in range(h)]
    long: list[int] = [[float('inf')] * w for _ in range(h)]
    prev: list[int] = [[None] * w for _ in range(h)]
    pq: list = []

    if h == 1:
        min_id = block[0].index(min(block[0]))
        block[0][min_id] = " "
        # print(block[0])
        block[0] = ''.join(map(str, block[0]))
        print(block[0])
        print('\n')
        # sys.exit(1)
        continue



    for i in range(w):
        heapq.heappush(pq, (block[0][i], 0, i, 1)) #(dist(strength), x, y, long)
        dist[0][i] = block[0][i]
        long[0][i] = 1

    while pq:
        current_dist, x, y, length = heapq.heappop(pq)

        if current_dist > dist[x][y]:
            continue

        for dx, dy in directions:
            nx: int = x + dx
            ny: int = y + dy
            if (0 <= nx < h and 0 <= ny < w):
                new_dist = current_dist + block[nx][ny]
                if new_dist < dist[nx][ny] and length + 1 <= long[nx][ny]:
                    dist[nx][ny] = new_dist
                    prev[nx][ny] = (x,y)
                    long[nx][ny] = length + 1
                    heapq.heappush(pq, (new_dist, nx, ny, length + 1))

    # print(block[h-1][dist[h-1].index(min(dist[h-1]))])
    path: deque = deque()
    x: int = h-1
    y: int = dist[h-1].index(min(dist[h-1]))
    path.append((x, y))
    while True:
        x, y = prev[x][y]
        path.append((x, y))
        if x == 0:
            break
    
    while path:
        x, y = path.popleft()
        block[x][y] = " "
    for i in range(h):
        # block[i][path[i]] = " "
        block[i] = ''.join(map(str, block[i]))
    
    # print(path)
    # print(block)
    for j in range(h):
        print(block[j])

    # print(path)
    
    print('\n')



