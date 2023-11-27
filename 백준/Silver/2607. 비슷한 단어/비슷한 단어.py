n = int(input())
words = [list(input()) for _ in range(n)]

target = words[0]
words = words[1:]
result = 0

for word in words:
    temp = target[:]
    cnt = 0
    for w in word:
        if w in temp:
            temp.remove(w)
        else:
            cnt += 1

    if cnt <= 1 and len(temp) <= 1:
        result += 1
print(result)