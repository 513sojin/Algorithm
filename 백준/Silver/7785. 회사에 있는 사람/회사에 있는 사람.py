n = int(input())
names = {}

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        names[name] = True
    else:
        del names[name]
        
temp = sorted(names.keys(), reverse=True)

for i in temp:
    print(i)