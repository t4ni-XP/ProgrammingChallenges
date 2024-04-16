r = int(input())
xy = [map(float, input().split()) for _ in range(r)]
x, y = [list(i) for i in zip(*xy)]
sum = 0
for i in range(r):
    sum += x[i]*y[i]
print(sum)