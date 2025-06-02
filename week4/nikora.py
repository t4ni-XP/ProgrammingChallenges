from collections import deque
n: int = int(input())
squares: list[int] = []
for _ in range(n):
    squares.append(int(input()))

# print(squares)
costs: list[int] = [float("inf")]*n
# print(costs)
jumps: deque = deque()

costs[1] = squares[1]
jumps.append([1,1]) #[current_position, jump_dist]

while jumps:
    jump = jumps.popleft()
    current = jump[0]
    dist = jump[1]
    forward = current + dist + 1
    backward = current - dist
    re_forward = current + 1

    if forward < n and costs[forward] > costs[current] + squares[forward]:
        costs[forward] = costs[current] + squares[forward]
        jumps.append((forward, dist + 1))
    if backward >= 0 and costs[backward] > costs[current] + squares[backward]:
        costs[backward] = costs[current] + squares[backward]
        jumps.append((backward, dist))
    if re_forward < n and costs[re_forward] > costs[current] + costs[backward] + squares[re_forward]:
        costs[re_forward] = costs[current] + costs[backward] + squares[re_forward]
        jumps.append((re_forward, dist + 1))

print(costs[n-1])



            
        
