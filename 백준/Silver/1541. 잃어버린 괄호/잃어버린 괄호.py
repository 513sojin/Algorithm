arr = input().split('-')

total = 0

for i in arr[0].split('+'):
    total += int(i)

for item in arr[1:]:
    for j in item.split('+'):
        total -= int(j)

print(total)