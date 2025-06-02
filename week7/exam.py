import sys
input = sys.stdin.readline

k: int = int(input())
ans: str = input()
f_ans: str = input()
ans_len = len(ans) - 1

# print(f_ans) 
count: int = 0
for i in range(len(ans)-1):
    if ans[i] == f_ans[i]:
        count += 1

point = min(k, count) + min(ans_len - k, ans_len- count)
# print(k)
# print(count)
# print(ans_len)
print(point)