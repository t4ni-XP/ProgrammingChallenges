def find_max_n(s):
    n = len(s)
    for i in range(1, n + 1):
        if n % i == 0:
            substring = s[:i]
            repeat_count = n // i
            if substring * repeat_count == s:
                return repeat_count
    return 1

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    for s in data:
        if s == ".":
            break
        max_n = find_max_n(s)
        print(max_n)

if __name__ == "__main__":
    main()
