n, k = map(int, input().split())
count = 0

while n >= k:
    count += 1

    if n % k == 0:
        n = n // k
    else:
        n = n - 1

count += n - 1

print(count)