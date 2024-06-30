import sys
input = sys.stdin.readline

n: int = int(input())

cubes: list = [i**3 for i in range(80)]
sum_set: set = set()
result: set = set()

# print(cubes)

for i in range(len(cubes)):
    for j in range(i, len(cubes)):
        cubes_sum = cubes[i] + cubes[j]
        if cubes_sum in sum_set:
            result.add(cubes_sum)
            # print(cubes[i],cubes[j])
        else:
            sum_set.add(cubes_sum)

sum_list = sorted(result)
# print(sum_list)
max_taxi_num: int = 0
for v in sum_list:
    if v <= n:
        max_taxi_num = v
    else:
        break




if max_taxi_num == 0:
    print("none")
else:
    print(max_taxi_num)
