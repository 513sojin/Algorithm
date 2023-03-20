n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

result = []

n_arr.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return result.append("yes")
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result.append("no")


for i in m_arr:
    binary_search(n_arr, i, 0, n - 1)

for i in result:
    print(i, end=' ')
