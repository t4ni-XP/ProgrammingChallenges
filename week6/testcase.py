import random

for _ in range(random.randint(1, 30)):
    # print(random.random())
    h = random.randint(1,5)
    w = random.randint(1,6)
    test_block = []
    for _ in range(h):
        line = [random.randint(1, 9) for _ in range(w)]
        line = ''.join(map(str, line))
        test_block.append(line)

    print(h, w)
    for j in range(h):
        print(test_block[j])

for _ in range(random.randint(1, 30)):
    # print(random.random())
    # h = random.randint(1,20)
    w = random.randint(1,60)
    h = 1
    test_block = []
    for _ in range(h):
        line = [random.randint(1, 9) for _ in range(w)]
        line = ''.join(map(str, line))
        test_block.append(line)

    print(h, w)
    for j in range(h):
        print(test_block[j])

print(0, 0)