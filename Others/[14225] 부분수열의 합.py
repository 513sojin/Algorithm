from itertools import combinations

n = int(input())
s = list(map(int, input().split()))

com = []
for i in range(1, n + 1):
    com += combinations(s, i)

arr_sum = []
for i in com:
    arr_sum.append(sum(i))

arr_sum = list(set(arr_sum))
arr_sum.sort()
answer = 1

for a in arr_sum:
    if a != answer:
        break
    answer += 1

print(answer)
