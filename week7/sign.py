import sys
input = sys.stdin.readline
from collections import deque

n: int = int(input())
# print(n)

test_cases = []
for _ in range(n):
    k, w = map(int, input().split())
    words: list[str] = [input().strip() for _ in range(w)]
    test_cases.append((k, w, words))

# print(test_cases)

for k, w, words in test_cases:
    current_chars: deque[str] = deque()
    min_chars: int = 0

    for word in words:
        last_id = 
        for char in word:
            if char not in current_chars:
                if len(current_chars) == k:
                    min_chars += 1
                    current_chars.popleft()
                current_chars.append(char)
                print(current_chars)
                continue
            current_id = current_chars.index(char)
            if current_id != last_id + 1:
                if len(current_chars) == k:
                    min_chars += 1
                    current_chars.popleft()
                current_chars.append(char)
                print(current_chars)
    
    print(min_chars + len(current_chars))

