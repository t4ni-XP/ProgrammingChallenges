n, m = map(int, input().split())
instruments: list[list[int]] = [list(map(int, input().split())) for _ in range(n)]
notes: list[int] = list(map(int, input().split()))

playable: list[set] = [set(instruments[i][1:]) for i in range(n)] #convert to List[set]
# print(instruments)
# print(tune)
# print(playable)

dp: list[list[int]] = [[float("inf")] * n for _ in range(m)]
# print(dp)

for inst in range(n):
    if notes[0] in playable[inst]:
        dp[0][inst] = 0

for i in range(1, m):
    for inst in range(n):
        if notes[i] in playable[inst]:
            if notes[i-1] in playable[inst]:
                dp[i][inst] = dp[i-1][inst]
            else:
                dp[i][inst] = min(dp[i-1]) + 1

print(min(dp[m-1]))
