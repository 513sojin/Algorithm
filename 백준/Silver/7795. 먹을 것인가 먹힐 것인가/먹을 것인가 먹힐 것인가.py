t = int(input())

def binarySearch(target, b):
    start = 0
    end = len(b) - 1
    res = -1

    while start <= end:
        mid = (start + end) // 2

        if b[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

for _ in range(t):
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    count = 0
    for i in a:
        count += binarySearch(i, b) + 1
    print(count)