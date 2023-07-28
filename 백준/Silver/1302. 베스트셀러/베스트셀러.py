from collections import Counter
n = int(input())
arr = [input() for _ in range(n)]

arr.sort()
count = Counter(arr)
sorted(count.items(), key = lambda x : x[1])

print(count.most_common()[0][0])