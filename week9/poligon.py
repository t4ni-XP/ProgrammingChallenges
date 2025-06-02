import sys
input = sys.stdin.readline
import math

n: int = int(input())
polygons: list[list[tuple]] = []
for _ in range(n):
    # Number of points in the polygon
    num_list: list[int] = list(map(int, input().split()))
    m: int = num_list[0]
    vertices: list[tuple] = []
    index = 1
    for _ in range(m):
        x = int(num_list[index])
        y = int(num_list[index + 1])
        vertices.append((x, y))
        index += 2
    polygons.append(vertices)
    
for vertices in polygons:
    m = len(vertices)
    area = 0
    for i in range(m-1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i+1]
        da = x1 * y2 - x2 * y1
        # print(da)
        area += da
    x1, y1 = vertices[m-1]
    x2, y2 = vertices[0]
    area += x1 * y2 - x2 * y1
    area = area / 2
    if area % 1 == 0:
        area = int(area)
    print(area)