import sys
input = sys.stdin.readline


testcases: list[dict] = []
n: int = int(input())
for _ in range(n):
    k, w = map(int, input().split())
    wards = []
    for _ in range(w):
        wards.append(input().split()[0])
    testcases.append([k, w, wards])

for case in testcases:
    print(case)
    k, w, words = case
    dp = [float("inf")] * w
    dp[0] = k
    results = []

    for i in range(w):
        for j in range(i + 1, w):
            print(words[i], words[j])
            overlap = 0
            for l in range(1,k):
                print(words[i][-l:], words[j][:l])
                if words[i][-l:] == words[j][:l]:
                        overlap = l
                # else:
                #      break
            print(overlap)
            dp[j] = min(dp[j], dp[i] + (k - overlap))
            print("--------")
    print(dp)
        