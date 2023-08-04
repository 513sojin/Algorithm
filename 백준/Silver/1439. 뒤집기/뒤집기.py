s = list(input())

zeroCnt = 0
oneCnt = 0

prev = s[0]

while s:
    i = int(s.pop(0))

    if prev != i:
        if i:
            oneCnt += 1
        else:
            zeroCnt +=1

    prev = i

print(oneCnt if oneCnt < zeroCnt else zeroCnt)