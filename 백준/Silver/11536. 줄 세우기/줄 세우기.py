n = int(input())
name = [input() for _ in range(n)]

if name == sorted(name):
    print('INCREASING')
elif name == sorted(name, reverse= True):
    print('DECREASING')
else:
    print('NEITHER')
