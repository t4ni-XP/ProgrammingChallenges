def get_prefix(name: str):
    return name[:2]

AllList: list[list[str]] = []

while True:
    n: int = int(input())  # nは入力回数
    if n == 0:
        break
    name_list: list[str] = [input() for _ in range(n)]
    sortedList = sorted(name_list, key=get_prefix)
    AllList.append(sortedList)
    # print(sortedList)

# print(AllList)
for i in range(len(AllList)):
    for j in range(len(AllList[i])):
        print(AllList[i][j])
    if i < len(AllList)-1:
        print("\n")