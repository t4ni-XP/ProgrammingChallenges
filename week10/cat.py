import sys
input = sys.stdin.readline

n: int = int(input())
mice: list[tuple] = []
for _ in range(n):
    x, y, s = input().split()
    mice.append((x, y, s))
m: float = float(input())

# print(m)

