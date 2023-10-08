n = int(input())
numbers = [input() for _ in range(n)]

length = len(numbers[0])

for i in range(1, length+1):
    temp = set()
    for num in numbers:
        temp.add(num[-i:])

    if len(temp) == len(numbers):
        print(i)
        exit()