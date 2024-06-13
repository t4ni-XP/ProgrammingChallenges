import sys
input = sys.stdin.readline
number: str = str(input().strip())
# number = str(1000) #debug
# number_len: int = len(number)
# state: str = "up"
# flag = 0

# for i in range(number_len - 1):
#     if int(number[i]) < int(number[i + 1]):
#         if state == "down":
#             flag = 1
#             break
#     if int(number[i]) > int(number[i + 1]):
#         state = "down"

# print(flag)
# if flag == 1:
#     print(-1)
# else:
count = 0
dp_up = set()#{"00", "000"}
dp_down = set() #{"00", "000"}
dp_eq = set()
# for k in range(number_len):
#     # dp_up.add("0"*k)
#     # dp_down.add("0"*k)
#     dp_eq.add("0"*k)
for j in range(int(number) + 1):
    num: int = j
    str_num: str = str(j)
    num_len = len(str(num))
    dp_eq.add("0"*num_len)
    f = 0
    if num_len == 1:
        count += 1
        dp_up.add(str_num)
        dp_down.add(str_num)
    elif num_len == 2:
        if str_num[0] == str_num[1]:
            count += 1
            # dp_up.add(str_num)
            # dp_down.add(str_num)
            dp_eq.add(str_num)
        elif str_num[0] < str_num[1]:
            count += 1
            dp_up.add(str_num)
        elif str_num[0] > str_num[1]:
            count += 1
            dp_down.add(str_num)
            # print("add", str_num)
    else:
        if str_num[0] == str_num[1]:
            if str_num[1:num_len] in dp_eq:
                count += 1
                dp_eq.add(str_num)
            elif str_num[1:num_len] in dp_up:
                count += 1
                dp_up.add(str_num)
            elif str_num[1:num_len] in dp_down:
                count += 1
                dp_down.add(str_num)
        elif str_num[0] < str_num[1]:
            if str_num[1:num_len] in dp_eq:
                count += 1
                dp_up.add(str_num)
            elif str_num[1:num_len] in dp_up:
                count += 1
                # f = 1
                dp_up.add(str_num)
            elif str_num[1:num_len] in dp_down:
                # if f != 1:
                count += 1
                dp_up.add(str_num)
        elif str_num[0] > str_num[1]:
            if str_num[1:num_len] in dp_eq:
                count += 1
                dp_down.add(str_num)
            elif str_num[1:num_len] in dp_down:
                count += 1
                dp_down.add(str_num)
            # continue
print(count)
union_set = dp_up.union(dp_down)
# print(number_len)
# # print("11000000" in union_set)
# print("22" in dp_up)
# print("22" in dp_down)
# print("22" in dp_eq)
# print(len(union_set))
# print(union_set)
# print(dp_up)
# print(dp_down)


