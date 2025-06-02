n: int = int(input())
testcases = []
for _ in range(n):
    sizes: list[int] = []
    number: int = int(input())
    data = input().split()
    sizes = [[int(data[i]), int(data[i + 1])] for i in range(0, len(data), 2)]
    testcases.append({
        "number": number,
        "sizes": sizes
    })

# print(testcases)

for case in testcases:
    n = case["number"]
    sizes = case["sizes"]
    sizes.sort(reverse = True)
    # print("-----")
    # print(sizes)
    current_dolls = []
    for doll in sizes:
        flag = False
        if len(current_dolls) == 0:
            current_dolls.append(doll)
        else:
            for i in range(len(current_dolls)):
                # print("{}と{}を比較してます".format(doll, current_dolls[i]))
                if current_dolls[i][0] > doll[0] and current_dolls[i][1] > doll[1]:
                    # print("{}を{}にいれます".format(doll, current_dolls[i]))
                    current_dolls[i] = doll
                    flag = True
                    # print("現在のリストの中身:{}".format(current_dolls))
                    break
            if flag == False:
                current_dolls.append(doll)
                # print("{}をリストに格納します".format(doll))
                # print("現在のリストの中身:{}".format(current_dolls))

    # print(current_dolls)
    print(len(current_dolls))