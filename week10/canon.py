import sys
input = sys.stdin.readline
import math
import heapq

x, y = list(map(float, input().split()))
start: tuple = (x, y)
x, y = list(map(float, input().split()))
destination: tuple = (x, y)
n:int = int(input())
cannon_list: list[tuple] = []
for _ in range(n):
    x, y = list(map(float, input().split()))
    cannon_list.append((x, y))

costs = [[] for _ in range(n + 2)] #n+2の配列を生成，内部に(node, cost)のタプルを入れる

###start -> destination cost calc
dist: float = (start[0] - destination[0]) ** 2 + (start[1] - destination[1]) ** 2
sqrt_dist: float = math.sqrt(dist)
cost: float = sqrt_dist / 5
node_cost: tuple = (n + 1, cost)
costs[0].append(node_cost)
for i in range(n):
    # start (<)-> node[i] cost calc
    dist = (start[0] - cannon_list[i][0]) ** 2 + (start[1] - cannon_list[i][1]) ** 2
    sqrt_dist  = math.sqrt(dist)
    cost = sqrt_dist / 5
    node_cost = (i + 1, cost)
    costs[0].append(node_cost)
    # node_cost = (0, cost)
    # costs[i + 1].append(node_cost)

    ### node[i] (<)-> destination cost calc
    dist = ((cannon_list[i][0] - destination[0]) ** 2 + (cannon_list[i][1] - destination[1]) ** 2)
    sqrt_dist: float = math.sqrt(dist)
    if sqrt_dist <= 30:
        cost = sqrt_dist / 5
    elif sqrt_dist >= 50:
        cost = (sqrt_dist - 50) / 5 + 2
    else:
        cost = (50 - sqrt_dist) / 5 + 2
    node_cost = (n + 1, cost)
    costs[i + 1].append(node_cost)

    ### node[i] <-> node[j] cost calc 
    for j in range(i + 1, n):
        dist = (cannon_list[i][0] - cannon_list[j][0]) ** 2 + (cannon_list[i][1] - cannon_list[j][1]) ** 2
        sqrt_dist = math.sqrt(dist)
        if sqrt_dist <= 30:
            cost = sqrt_dist / 5
        elif sqrt_dist >= 50:
            cost = (sqrt_dist - 50) / 5 + 2
        else:
            cost = (50 - sqrt_dist) / 5 + 2
        node_cost = (j + 1, cost)
        costs[i + 1].append(node_cost)
        node_cost = (i + 1, cost)
        costs[j + 1].append(node_cost)

# print(costs)

### ダイクストラ法で最短経路を求める
nodes = [float('inf')] * (n + 2)
nodes[0] = 0
node_name = []
heapq.heappush(node_name, 0)

while len(node_name) != 0:
    min_point = heapq.heappop(node_name)

    for edge in costs[min_point]:
        dest = edge[0]
        cost  = edge[1]

        if nodes[min_point] + cost < nodes[dest]:
            nodes[dest] = nodes[min_point] + cost
            heapq.heappush(node_name, dest)

print(nodes[n+1])





# print(start)