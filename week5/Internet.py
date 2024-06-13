import sys
sys.setrecursionlimit(200000)  # 再帰深度を2000に設定


n, m = map(int, input().split())
# print(n, m)
edge: list[list[int]]=[[] for i in range(n+1)]
# print(edge)
for _ in range(m):
    A, B = map(int, input().split())
    # if A <= B:
    #     edge[A].append(B)
    # else:
    #     edge[B].append(A)
    edge[A].append(B)
    edge[B].append(A)
# print(edge)
visited: set[int] = set()

def dfs(start_node):
    # print("start node is{}".format(start_node))
    visited.add(start_node)
    for i in range(len(edge[start_node])):
        next_node = edge[start_node][i]
        if next_node not in visited:
            dfs(next_node)

dfs(1)
# print(visited)
# not_visited = []
flag = 0
for i in range(1,n+1):
    if i not in visited:
        # not_visited.append(i)
        print(i)
        flag = 1

if flag == 0:
    print("Connected")

# print(not_visited)