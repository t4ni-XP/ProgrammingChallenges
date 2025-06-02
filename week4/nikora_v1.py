n: int = int(input())
squares: list[int] = []
for _ in range(n):
    squares.append(int(input()))

# print(squares)
costs: list[int] = [0]*n
pre_dist: list[int] = [0]*n
costs[n-1] = float("inf")

costs[1] = squares[1]
pre_dist[1] = 1
for _ in range(1, n):
    # if costs[n-1] != 0:
    #     break
    for i in range(len(pre_dist)):
        if pre_dist[i] == 0:
            continue
        # print(costs)
        # print(pre_dist)
        dist = pre_dist[i]
        forward = i + dist + 1
        backward = i - dist
        if forward == n-1:
            # print("critical at [{},{}]".format(i, dist))
            if costs[forward] > costs[i] + squares[forward]:
                costs[forward] = costs[i] + squares[forward]
                # print("target pos is changed")
                continue
            else:
                pre_dist[i] = 0
                continue
        if dist == 0:
            continue
        if forward >= n and backward < 0:
            pre_dist[i] = 0
            continue
        if forward < n:
            costs[forward] = costs[i] + squares[forward]
            pre_dist[forward] = dist + 1
            if backward >= 0:
                costs[backward] = costs[i] + squares[backward]
                pre_dist[backward] = dist
            continue
        if backward >= 0:
            costs[backward] = costs[i] + squares[backward]
            pre_dist[backward] = dist
            if forward < n:
                costs[forward] = costs[i] + squares[forward]
                pre_dist[forward] = dist + 1
            continue
        if costs[n-1] != 0:
            break

print(costs[n-1])