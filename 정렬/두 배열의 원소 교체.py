
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = sorted(a)
sorted_b = sorted(b)

result = 0

for i in range(k):
    if sorted_a[i] < sorted_b[len(b) - (1 + i)]:
        sorted_a[i], sorted_b[len(b) - (1 + i)] = sorted_b[len(b) - (1 + i)], sorted_a[i]

for i in sorted_a:
    result += i

print(result)