num_list = []
# for _ in range(4):
#     num_list.append(list(map(int, input().split())))
try:
    while True:
        line = input()
        if line.strip() == "":
            break
        k, n = map(int, line.split())
        num_list.append([k, n])
except EOFError:
    pass

# print(num_list)

# def tight_words(k, n):
#     if n == 1:
#         return k
#     else:
#         return(tight_words(k n-1))


for sequence in num_list:
    k = sequence[0]
    n = sequence[1]
    if n == 0:
        print(0)
        continue
    if k == 0:
        print(100)
        continue
    dp = [[0] * (k + 1) for _ in range(n)]
    for i in range(k + 1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(k + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == k:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    # print(dp)
    
    tight_words: int = sum(dp[n-1])
    all_words: int = (k+1) ** n
    ratio: int = tight_words/all_words * 100
    ratio = round(ratio, 8)
    print(ratio)

