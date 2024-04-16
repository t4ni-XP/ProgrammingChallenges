str = input()
numbers = str.split()
n = int(numbers[2])
x = int(numbers[0])
y = int(numbers[1])
for i in range(n+1):
    if i == 0:
        continue
    if i % x == 0 and i % y == 0:
        print("FizzBuzz")
    elif i % x == 0 : 
        print ("Fizz")
    elif i % y == 0:
        print ("Buzz")
    else :
        print(i)
