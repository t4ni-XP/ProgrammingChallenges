info = [int(input()) for i in range(2)]
pi = [int(input()) for i in range(info[1])]
allGigas = info[0] * (info[1]+1)
usedGigas = sum(pi)
print(allGigas-usedGigas)