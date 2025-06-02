def minimum_scrolled_letters(n, cases):
    results = []
    
    for k, w, words in cases:
        # dp[i] は、i 番目の単語を表示するために必要な最小のスクロール数
        dp = [0] * w
        
        # 最初の単語はそのまま表示
        dp[0] = k
        
        for i in range(1, w):
            # i 番目の単語を表示するために必要な文字数を計算
            overlap = 0
            # オーバーラップを計算
            for j in range(1, k):
                if words[i-1][k-j:] == words[i][:j]:
                    overlap = j
            dp[i] = dp[i-1] + (k - overlap)
        
        results.append(dp[-1])
    
    for result in results:
        print(result)

# メインの実行部分
n = int(input().strip())  # テストケースの数を読み込む

cases = []
for _ in range(n):
    k, w = map(int, input().strip().split())  # k と w を読み込む
    words = [input().strip() for _ in range(w)]  # w 個の単語を読み込む
    cases.append((k, w, words))

# 各テストケースを処理し、結果を出力する
minimum_scrolled_letters(n, cases)
