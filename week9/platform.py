import sys
input = sys.stdin.readline

n = int(input())
platforms = []
for _ in range(n):
    h, x, y = map(int, input().split())
    platforms.append((h, x, y))

platforms.sort()
# print(platforms)
built = []
# print(platforms[1][1])
ans = 0
for platform in platforms:
    # print(platform)
    # print(built)
    left_leg = 0
    right_leg = 0
    for built_plat in reversed(built):
        # print("--built_plat--")
        # print(built_plat)
        if left_leg != 0 and right_leg != 0:
            break
        if platform[2] < built_plat[1] or platform[1] > built_plat[2]:
            continue
        if built_plat[1] <= platform[1] < built_plat[2] and left_leg == 0:
            left_leg = platform[0] - built_plat[0]
            # print("left_leg = ",left_leg)
        if built_plat[1] < platform[2] <= built_plat[2] and right_leg == 0:
            right_leg = platform[0] - built_plat[0]
            # print("right_leg = ",right_leg)
        # print("------")
    if left_leg == 0:
        left_leg = platform[0]
    if right_leg == 0:
        right_leg = platform[0]
    # print("left_leg = ",left_leg)
    # print("right_leg = ",right_leg)

    ans += left_leg + right_leg
    built.append(platform)
    # print("ans = ",ans)
    # print("--------")

print(ans)

