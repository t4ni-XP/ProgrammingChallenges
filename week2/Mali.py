n = int(input())  # nは入力回数
num_list = []
for i in range(n):
    num_list.append(list(map(int,input().split())))
maximal_sum: int = sum(num_list[0])
current_min: int = min(num_list[0])
current_max: int = max(num_list[0])
for i in range(n):
    if i == 0:
        continue
    new_min: int = min(num_list[i])
    new_max: int = max(num_list[i])
    current_min = current_min if current_min < new_min else new_min
    current_max = current_max if current_max > new_max else new_max