import sys
input = sys.stdin.readline
n = int(input().strip())

s = str(n)
increasing = True
flag = 0
for i in range(1, len(s)):
    if increasing:
        if s[i] < s[i-1]:
            increasing = False
    if not increasing:
        if s[i] > s[i-1]:
            flag = 1
            break

if flag == 1:
    print(-1)
else:
    length = len(s)
    dp = [[[0] * 3 for _ in range(10)] for _ in range(length + 1)]
    for i in range(10):
        dp[1][i][0] = 1
        dp[1][i][1] = 1
        dp[1][i][2] = 1
    for j in range(2, length + 1):
        for k in range(10):
            # strictly increasing
            dp[j][k][0] = sum(dp[j-1][l][0] for l in range(k))
            # flat/increasing
            dp[j][k][1] = dp[j-1][k][0] + dp[j-1][k][1]
            # decreasing
            dp[j][k][2] = sum(dp[j-1][l][1] + dp[j-1][l][2] for l in range(k, 10))

print(dp[2][4])
