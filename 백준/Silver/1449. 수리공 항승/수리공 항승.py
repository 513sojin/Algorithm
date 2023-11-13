import sys
input = sys.stdin.readline

n,l = map(int, input().split())
lengths = list(map(int,input().split()))
lengths.sort()

result = 1
start = lengths[0]

for i in lengths[1:]:
    if i - start + 1 > l:
        result += 1
        start = i

print(result)