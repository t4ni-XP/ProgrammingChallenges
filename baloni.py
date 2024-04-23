n: int = int(input())
balloons: list[int] = list(map(int, input().split()))
balloonsSet: set = set(balloons)
# print(balloons)

count: int = 0
delCount: int = 0
while len(balloons) != 0:
    head: int = balloons[0]
    # print("while1-----")
    # print("head:"+str(head))
    del balloons[0]
    # print(balloons)
    count += 1
    delCount += 1
    # print("count:"+str(count))
    i: int = 0
    # print("while2----")
    while len(balloons) > 0 and i < n- delCount:
        if head - 1 not in balloonsSet:
            break
        if(balloons[i] == head-1):
            head = head -1
            del balloons[i]
            delCount += 1
            # print("head :"+str(head))
        else:
            i +=1
            # print("i:"+str(i))

print(count)
    
    