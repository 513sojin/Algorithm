n, m = map(int, input().split())
names = {}

for _ in range(n+m):
    name = input()
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

result = list(filter(lambda x: names[x] > 1, names))

print(len(result))
result.sort()
for name in result:
    print(name)