n = int(input())
arr = []
result = []
final_result = []

for i in range(n):
    arr.append(list(map(str, input().split())))

def quick_sort(array):
    if len(array) < 1:
        return array

    pivot = array[0][1]
    tail_arr = array[1:]

    left_arr = [x for x in tail_arr if int(x[1]) <= int(pivot)]
    right_arr = [x for x in tail_arr if int(x[1]) > int(pivot)]

    return quick_sort(left_arr) + [array[0]] + quick_sort(right_arr)

result = quick_sort(arr)

for i in result:
    final_result.append(i[0])

print(final_result)