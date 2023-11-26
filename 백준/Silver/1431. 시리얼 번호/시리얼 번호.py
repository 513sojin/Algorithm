n = int(input())
numbers = [input() for _ in range(n)]
answer = []

for n in numbers:
    result = 0
    for i in n:
        if i.isdigit():
            result += int(i)
    answer.append((n, result))

answer.sort(key= lambda x:(len(x[0]), x[1], x[0]))

for a in answer:
    print(a[0])