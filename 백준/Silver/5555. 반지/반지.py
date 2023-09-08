s = input()
n = int(input())
result = 0

for i in range(n):
    text = input()
    text += text

    if s in text:
        result += 1

print(result)