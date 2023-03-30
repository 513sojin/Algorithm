# 상하좌우

x = 1
y = 1

n = int(input())
list = list(map(str, input().split()))

for d in list:
    if d == "R" and y + 1 <= n:
        y += 1
    elif d == "L" and y - 1 >= 1:
        y -= 1
    elif d == "U" and x - 1 >= 1:
        x -= 1
    elif d == "D" and x + 1 <= n:
        x += 1

print(x, y)


# 정리
# 위치의 변화 값을 배열에 넣는 접근이 좋아보인다.
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0 ,0]
# types = ['L','R','U','D'] 이런식으로

