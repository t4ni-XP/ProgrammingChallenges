import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# print(n)

numbers:list[bool] = [True]*(n+1)
# print(numbers)
if len(numbers) > 1:
    numbers[0] = False
if len(numbers) > 2:
    numbers[1] = False
if len(numbers) < 2:
    exit()
count: int = 0
# print(numbers)
# print(len(numbers))
for i in range(2, len(numbers)):
    if count == k:
        break
    if numbers[i] == True:
        # print(i)
        # if count == k:
        #     print(i)
        #     print(numbers)
        #     break
        m:int = n // i
        # print(m)
        if n < 2:
            continue
        for j in range(1, m + 1):
            if numbers[i * j] == True:
                count += 1
            numbers[i * j] = False
            # print(numbers)
            if count == k:
                print(i * j)
                # print(numbers)
                # exit()
                break