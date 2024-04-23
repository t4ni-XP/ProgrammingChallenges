n: int = int(input())
balloons: list[int] = list(map(int, input().split()))
# print(balloons)

count: int = 0
while len(balloons) != 0:
    head: int = balloons[0]
    del balloons[0]
    count += 1
    while head-1 in balloons:
        balloons.remove(head-1)
        head = head-1

print(count)
    
    