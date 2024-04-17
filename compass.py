info = [int(input()) for i in range(2)]
flag = info[0] > info[1]
if flag == 1:
    if info[0] - info[1] > 180:
        print(-(info[1] + 360 - info[0]))
    else:
        print(info[0] - info[1])
else:
    if info[1] - info[0] > 180:
        print(-(info[0] + 360 - info[1]))
    else:
        print(info[1] - info[0])
