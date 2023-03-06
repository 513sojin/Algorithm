# 숫자 카드 게임

N, M = map(int, input().split())
result = 0

for i in range(N):
    array = list(map(int, input().split()))
    arr_min = min(array)

    if result < arr_min:
        result = arr_min

print(result)

