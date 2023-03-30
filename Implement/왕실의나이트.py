dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

d = input()
x = ord(d[0]) - 96
y = int(d[1])

count = 0

for i in range(8):
    if x + dx[i] < 1 or x + dx[i] > 8 or y + dy[i] < 1 or y + dy[i] > 8:
        continue
    count += 1

print(count)