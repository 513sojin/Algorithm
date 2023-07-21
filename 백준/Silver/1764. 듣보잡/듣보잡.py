n, m = map(int, input().split())
arr_n = set()
arr_m = set()

for _ in range(n):
    arr_n.add(input())

for _ in range(m):
    arr_m.add(input())

result = list(arr_n.intersection(arr_m))
result.sort()

print(len(result))
for name in result:
    print(name)