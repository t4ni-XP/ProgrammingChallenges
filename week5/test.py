from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def solve():
    number_of_testcase = int(input())
    results = []

    for _ in range(number_of_testcase):
        n, m = map(int, input().split())
        lab_list = list(map(int, input().split()))
        edges = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        
        for _ in range(m):
            A, B = map(int, input().split())
            indegree[B-1] += 1
            edges[A-1].append(B-1)
        
        # Topological Sort with minimal lab switches
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        lab_count = defaultdict(int)
        topo_order = []

        while q:
            node = q.popleft()
            topo_order.append(node)
            lab_count[lab_list[node]] += 1
            
            for neighbor in edges[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # Calculate minimum lab switches
        current_lab = -1
        move_count = 0
        
        for node in topo_order:
            if lab_list[node] != current_lab:
                move_count += 1
                current_lab = lab_list[node]

        results.append(move_count - 1)  # Subtract the initial move count

    for result in results:
        print(result)

solve()
