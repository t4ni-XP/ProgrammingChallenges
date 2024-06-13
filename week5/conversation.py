from collections import deque
import sys
input = sys.stdin.readline

number_of_testcase: int = int(input())
testcases = []
for _ in range(number_of_testcase):
    n, m = map(int, input().split())
    # lab: list[int] = []
    # lab_list = [0]
    # lab_list_ex: list[int] = list(map(int, input().split()))
    # lab_list.extend(lab_list_ex)
    # lab.append(lab_list)
    lab_list: list[int] = list(map(int, input().split()))
    edges = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]
    for _ in range(m):
        # print("edge input")
        A, B = map(int, input().split())
        indegree[B-1] += 1
        edges[A-1].append(B)
    testcases.append({
        "n" : n,
        "m" : m,
        "lab_list" : lab_list,
        "edges" : edges,
        "indegree" : indegree
    })

# print(testcases)

for case in testcases:
    counts = []
    for l in range(1,3):
        # print(i)
        count =  0
        q = deque()
        n = case["n"]                  # the number of conservation stages
        m = case["m"]                  # the number of dependencies between them
        lab_list = case["lab_list"]
        edges = case["edges"]
        indegree = case["indegree"]

        for i in range(n):
            if(indegree[i] == 0):
                q.append(i)
        # print(q)

        before:int = l
        s_list = []
        while len(q) != 0:
            if(len(q) == 1):
                u = q.popleft()
                # print("lab_list[u]",lab_list[u], "lab_list[before]",lab_list[before])
                if lab_list[u] != before:
                    count += 1
                for i in edges[u]:
                    indegree[i-1] -= 1
                    if indegree[i-1] == 0:
                        q.append(i-1)
                before = lab_list[u]
                # print("statement:", 1)
                # print(indegree,u, q, count)
            else:
                for i in range(len(q)):
                    temp = q[i]
                    # print("lab_list[temp]",lab_list[temp], "lab_list[before]",lab_list[before])
                    if lab_list[temp] == before:
                        u = temp
                        del q[i]
                        for i in edges[u]:
                            indegree[i-1] -= 1
                            if indegree[i-1] == 0:
                                q.append(i-1)
                        before = lab_list[u]
                        # print("statement:", 2)
                        # print(indegree, u, q, count)
                        break
                else:
                    u = q.popleft()
                    count += 1
                    for i in edges[u]:
                        indegree[i-1] -= 1
                        if indegree[i-1] == 0:
                            q.append(i-1)
                    before = lab_list[u]
                    # print("statement:", 3)
                    # print(indegree,u,q, count)
                continue
        counts.append(count)
    
    print(min(counts))
    # print(s_list)




