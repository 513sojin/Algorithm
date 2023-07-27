n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

min_bundle = sorted(arr, key = lambda x: x[0])[0][0]
min_single = sorted(arr, key= lambda x : x[1])[0][1]

if n <= 6:
    print(min(min_single * n, min_bundle))
else:
    print(min(n//6 * min_bundle + min_bundle, n * min_single, n//6 * min_bundle + (n%6) * min_single ))