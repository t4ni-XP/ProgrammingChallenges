count = 0
def probability_of_sum(N, T, numbers):
    # ダイナミックプログラミング用のテーブルを初期化
    dp = [0] * (T + 1)
    dp[0] = 1  # 和が0の確率は1

    for num in numbers:
        # テーブルを更新
        for j in range(T, num - 1, -1):
            dp[j] += dp[j - num]

    # 和がTとなる確率を取得
    return dp[T] / (len(numbers) ** N)  # 全ての組み合わせの数で割る



# input number of games
number_of_game = int(input())
games: list[dict] = []

# games = [{"m": number of tiles in the bag
#           "tiles": m labels of the tiles
#           "n": number of tiles that drawing out 
#           "t": target 
#           }, ...] 

# input each games
for _ in range(number_of_game):
    m = int(input())
    tiles = list(map(int, input().split()))
    n, t = map(int, input().split())
    games.append({
        "m": m,
        "tiles": tiles,
        "n": n,
        "t": t
    })

for game in games:
    print("確率:", probability_of_sum(game["n"], game["t"], game["tiles"]))