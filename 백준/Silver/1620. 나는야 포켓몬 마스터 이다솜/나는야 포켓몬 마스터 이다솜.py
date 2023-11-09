import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dict = {}
for i in range(1,n+1):
    a = input().strip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    temp = input().strip()
    if temp.isdigit():
        print(dict[int(temp)])
    else:
        print(dict[temp])