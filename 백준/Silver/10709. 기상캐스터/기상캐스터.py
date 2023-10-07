n,m = map(int, input().split())
clouds = [list(map(str,input().strip())) for _ in range(n)]
answer = [[0]*m for _ in range(n)]


for y in range(n):
    flag = False
    cnt = 0
    for x in range(m):
        if clouds[y][x] == 'c':
            flag = True
            answer[y][x] = 0
            cnt = 1
        elif not flag and clouds[y][x] == '.':
            answer[y][x] = -1
        elif flag and clouds[y][x] == '.':
            answer[y][x] = cnt
            cnt += 1

for ans in answer:
    print(*ans)