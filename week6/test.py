import sys
import heapq

def parse_input():
    blocks = []
    while True:
        h, w = map(int, input().strip().split())
        if h == 0 and w == 0:
            break
        block = []
        for _ in range(h):
            block.append(list(map(int, list(input().strip()))))
        blocks.append((h, w, block))
    return blocks

def dijkstra(h, w, block):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    dist = [[float('inf')] * w for _ in range(h)]
    prev = [[None] * w for _ in range(h)]
    pq = []
    
    for j in range(w):
        heapq.heappush(pq, (block[0][j], 0, j))
        dist[0][j] = block[0][j]
    
    while pq:
        current_dist, x, y = heapq.heappop(pq)
        
        if current_dist > dist[x][y]:
            continue
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                new_dist = current_dist + block[nx][ny]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    prev[nx][ny] = (x, y)
                    heapq.heappush(pq, (new_dist, nx, ny))
    
    min_dist = float('inf')
    min_pos = None
    for j in range(w):
        if dist[h-1][j] < min_dist:
            min_dist = dist[h-1][j]
            min_pos = (h-1, j)
    
    path = []
    while min_pos is not None:
        path.append(min_pos)
        min_pos = prev[min_pos[0]][min_pos[1]]
    
    return path

def print_block_with_path(h, w, block, path):
    block_copy = [row[:] for row in block]
    for x, y in path:
        block_copy[x][y] = ' '
    
    for row in block_copy:
        print(''.join(map(str, row)))
    print()

def main():
    blocks = parse_input()
    for h, w, block in blocks:
        path = dijkstra(h, w, block)
        print_block_with_path(h, w, block, path)

if __name__ == "__main__":
    main()
