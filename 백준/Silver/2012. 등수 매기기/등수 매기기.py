import sys
input = sys.stdin.readline

n = int(input())
score = []
result = 0

for _ in range(n):
    score.append(int(input()))

score.sort()
for i in range(1,n+1):
    result += abs(i - score[i-1])

print(result)