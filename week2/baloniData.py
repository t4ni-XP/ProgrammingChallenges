from random import randint

N = 10000
f = open("input.txt", "w")
print(N, file=f)
for _ in range(N):
    print(randint(1,N), end=' ', file=f)
f.close()
print()