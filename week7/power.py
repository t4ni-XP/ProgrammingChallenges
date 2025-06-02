import sys
input = sys.stdin.readline

strings: list[str] = []
while True:
    string = input()
    if string == ".\n":
        break
    strings.append(string[:-1])

for string in strings:
    n: int = len(string)
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(int(i))
    divisors.append(n)

    # print(divisors)
    for d in divisors:
        k: int = n // d
        # print(d, k)
        substring = string[:d] * k
        # print(substring)
        if substring == string:
            print(k)
            break