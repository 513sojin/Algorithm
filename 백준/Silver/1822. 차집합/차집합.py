import sys
input = sys.stdin.readline

a,b = map(int, input().split())
set_a = set(list(map(int, input().split())))
set_b = set(list(map(int, input().split())))

result = list(set_a - set_b)
if result:
    print(len(result))
    result.sort()
    print(*result)
else:
    print(0)
