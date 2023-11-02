import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    name,k,m,e = input().strip().split()
    arr.append((name,int(k),int(m),int(e)))

arr.sort(key= lambda x:(-x[1],x[2],-x[3],x[0]))

for name, _, _, _ in arr:
    print(name)