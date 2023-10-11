import sys

input = sys.stdin.readline
n,c = map(int, input().split())
nums = list(map(int, input().split()))

dict = {}
answer = []

for num in nums:
    if num not in dict:
        dict[num] = 1
    else:
        dict[num] += 1

for key,value in dict.items():
    answer.append([key,value])
answer.sort(key = lambda x : -x[1])

for key, cnt in answer:
    for _ in range(cnt):
        print(key, end= ' ')