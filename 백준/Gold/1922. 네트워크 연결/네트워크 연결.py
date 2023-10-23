import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = []
parent = [0] * (n+1)
result = 0

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union_find(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x

def check_same_parent(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    else:
        return False

for _ in range(m):
    graph.append(list(map(int, input().split())))

for i in range(1,n+1):
    parent[i] = i

graph.sort(key= lambda x:x[2])

for g in graph:
    if not check_same_parent(g[0], g[1]):
        union_find(g[0],g[1])
        result += g[2]

print(result)