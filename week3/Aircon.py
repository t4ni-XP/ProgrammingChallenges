n:int = int(input())  # nは入力回数
num_list: list[tuple] = []
for i in range(n):
    num_list.append(tuple(int(x)for x in input().split()))
# print(num_list)
num_list.sort(key=lambda x: (x[0],x[1]))
# print(num_list)
i: int = 0
count: int = 0
current: int = 0
while i < n:
    l,h = num_list[i]
    if l > current:
        count += 1
        current = h
    elif h  < current:
        current = h
    i += 1
print(count)