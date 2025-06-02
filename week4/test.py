n = int(input())
squares = [0] * n
for i in range(n):
    squares[i] = int(input())

costs = [float('inf')] * n
costs[0] = 0  # スタート地点のコストは0
costs[1] = squares[1]  # 最初のジャンプは必ず2に行く

from collections import deque
queue = deque([(1, 1)])  # (現在位置, 直前のジャンプの長さ)

while queue:
    pos, last_jump = queue.popleft()
    
    # 前方へのジャンプ
    forward = pos + last_jump + 1
    if forward < n and costs[forward] > costs[pos] + squares[forward]:
        costs[forward] = costs[pos] + squares[forward]
        queue.append((forward, last_jump + 1))
    
    # 後方へのジャンプ
    backward = pos - last_jump
    if backward > 0 and costs[backward] > costs[pos] + squares[backward]:
        costs[backward] = costs[pos] + squares[backward]
        queue.append((backward, last_jump))
    
    # 再度前方へのジャンプ
    re_forward = pos + last_jump
    if re_forward < n and costs[re_forward] > costs[pos] + squares[re_forward]:
        costs[re_forward] = costs[pos] + squares[re_forward]
        queue.append((re_forward, last_jump))

print(costs)