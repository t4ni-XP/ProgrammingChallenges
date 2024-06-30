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

# print(polygons)

# for vertices in polygons:
#     x1, y1 = vertices[0]
#     areas: list[int] = []
#     area = 0
#     for i in range(1, len(vertices)-1):
#         x2, y2 = vertices[i]
#         x3, y3 = vertices[i + 1]
#         dist_12 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#         dist_23 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
#         dist_31 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
#         z: int = (dist_12 + dist_23 + dist_31) / 2
#         s: int = math.sqrt(z * (z - dist_12) * (z - dist_23) * (z - dist_31))
#         s = round(s, 10)
#         s = int(s)
#         areas.append(s)

#         # x_list: list[int] = [x1, x2, x3]
#         # y_list: list[int] = [y1, y2, y3]
#         # x_min = min(x_list)
#         # x_max = max(x_list)
#         # y_min = min(y_list)
#         # y_max = max(y_list)
#         # rect_area: int = (x_max - x_min) * (y_max - y_min)

#     print(area)
    
for vertices in polygons:
    m = len(vertices)
    area = 0
    for i in range(m-1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i+1]
        area += x1 * y2 - x2 * y1
    area = area / 2
    if area % 1 == 0:
        area = int(area)
    print(area)