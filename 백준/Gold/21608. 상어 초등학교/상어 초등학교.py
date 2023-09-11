n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]
sit = [[0]*n for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for student in students:
    available = []

    for x in range(n):
        for y in range(n):
            if sit[x][y] == 0:
                # 아직 아무도 앉지 않았다면
                around, friend = 0, 0

                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y

                    if 0 <= nx < n and 0 <= ny < n:
                        if sit[nx][ny] in student[1:]:
                            friend += 1

                        if sit[nx][ny] == 0:
                            around += 1
                available.append((friend, around, x, y))
    available.sort(key= lambda x : (-x[0], -x[1], x[2], x[3]))
    sit[available[0][2]][available[0][3]] = student[0]

students.sort()
result = 0
score = [0,1,10,100,1000]
for x in range(n):
    for y in range(n):
        around = 0

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if sit[nx][ny] in students[sit[x][y]-1]:
                    around += 1

        result += score[around]

print(result)

