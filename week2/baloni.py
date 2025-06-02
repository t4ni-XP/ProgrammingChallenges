n: int = int(input())
balloons: list[int] = list(map(int, input().split()))
arrows: list[int]=[]
count: int = 0

for i in range(len(balloons)):
    if balloons[i] not in arrows:
        count += 1
        arrows.append(balloons[i]-1)
    else:
        arrows.remove(balloons[i])
        arrows.append(balloons[i]-1)


print(count)
    
    
