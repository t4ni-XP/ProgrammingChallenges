R,C = map(int, input().split())  # nは入力回数
city_map = [list(input()) for _ in range(R)]
# print(city_map)

output: list[int] = [0,0,0,0,0]


for i in range(C-1):
    for j in range(R-1):
        count: int = 0
        # print(i, j)
        if city_map[i][j]=='#' or city_map[i+1][j]=='#' or city_map[i][j+1]=='#' or city_map[i+1][j+1]=='#':
            continue
        if city_map[i][j]=='X':
            count += 1
        if city_map[i+1][j]=='X':
            count += 1                        
        if city_map[i][j+1]=='X':
            count += 1
        if city_map[i+1][j+1]=='X':
            count += 1
        # print("count:", count)
        output[count] += 1

# print(output)

for i in range(5):
    print(output[i])