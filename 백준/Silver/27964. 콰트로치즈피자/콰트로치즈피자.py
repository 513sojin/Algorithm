n = int(input())
name = list(input().split())
result = set()

for i in name:
    if i.endswith('Cheese'):
        result.add(i)

if len(result) >= 4:
    print('yummy')
else:
    print('sad')