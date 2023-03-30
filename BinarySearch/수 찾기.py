
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if a[mid] == target:
            return True
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in b:
    result = binary_search(0, len(a) - 1, i)
    if result:
        print(1)
    else:
        print(0)
