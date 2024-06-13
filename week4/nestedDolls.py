from bisect import bisect_right

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
    sizes.sort(key=lambda x: (x[0], -x[1]))
    # print("-----")
    # print(sizes)
    current_dolls = []

    for doll in sizes:
        height = doll[1]
        pos = bisect_right(current_dolls, height)
        if pos < len(current_dolls):
            current_dolls[pos] = height
        else:
            current_dolls.append(height)

    print(len(current_dolls))


