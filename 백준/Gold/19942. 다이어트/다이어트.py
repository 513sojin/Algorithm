n = int(input())
a,b,c,d = map(int, input().split()) # 단백질, 탄수화물, 지방, 비타민
arr = [list(map(int, input().split())) for _ in range(n)]

temp = []
result = []

def check(array):
    a1,b1,c1,d1 = 0,0,0,0
    for arr in array:
        a1 += arr[0]
        b1 += arr[1]
        c1 += arr[2]
        d1 += arr[3]

    if a1 >= a and b1 >= b and c1 >= c and d1 >= d:
        return True
    else:
        return False

def backtracking(start):
    if check(temp):
        money_list = [x[4] for x in temp]
        money = sum(money_list)
        result.append([x[5] + 1 for x in temp] + [money])
        return

    for i in range(start, len(arr)):
        temp.append(arr[i] + [i])
        backtracking(i+1)
        temp.pop()

backtracking(0)
result.sort(key = lambda x: x[-1])

if len(result) > 0:
    print(result[0][-1])
    print(' '.join(map(str, result[0][:-1])))
else:
    print(-1)