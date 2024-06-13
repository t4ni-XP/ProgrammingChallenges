import sys
from collections import deque

input = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x


    def same(self, x, y):
        return self.find(x) == self.find(y)

number_of_datasets = int(input())
datasets = []

for _ in range(number_of_datasets):
    N, M, L, number_of_S = map(int, input().split())
    S = deque(map(int, input().split()))
    edges = []
    for _ in range(M):
        s, t, w = map(int, input().split())
        edges.append((w, s, t))
    edges.sort()
    datasets.append({
        "N" : N,
        "M" : M,
        "L" : L,
        "number_of_S": number_of_S,
        "S" : S,
        "edges" : edges
    })

for dataset in datasets:
    N = dataset["N"]
    M = dataset["M"]
    L = dataset["L"]
    number_of_S = dataset["number_of_S"]
    S = dataset["S"]
    edges = dataset["edges"]

    uf = UnionFind(N)
    while len(S) > 1:
        A = S.popleft()
        uf.union(A - 1, S[0] - 1)
    
    cost = 0
    count = 0 #edgeの数
    for edge in edges:
        w, s, t = edge
        if not uf.same(s - 1, t - 1):
            cost += w
            count += 1
            uf.union(s - 1, t - 1)
    print(cost + count * L)




