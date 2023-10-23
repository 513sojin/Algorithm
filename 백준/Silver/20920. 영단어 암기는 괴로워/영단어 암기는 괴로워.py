import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dict = {}

words_sort = []
for _ in range(n):
    temp = input().strip()
    if len(temp) >= m:
        words_sort.append(temp)

words_sort.sort()

for word in words_sort:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

dict = sorted(dict.items(), key=lambda x:(-x[1], -len(x[0])))

for key, value in dict:
    print(key)
