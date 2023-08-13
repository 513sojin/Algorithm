import sys
input = sys.stdin.readline

n = int(input())

graph = [list(input().split()) for _ in range(n)]
teachers = []
result = ''

def findStudents():
    for teacher in teachers:
        x, y = teacher

        for i in range(x-1, -1,-1):
            if graph[i][y] == 'O':
                break
            elif graph[i][y] == 'S':
                return False

        for i in range(x+1, n):
            if graph[i][y] == 'O':
                break
            elif graph[i][y] == 'S':
                return False

        for i in range(y-1, -1, -1):
            if graph[x][i] == 'O':
                break
            elif graph[x][i] == 'S':
                return False

        for i in range(y+1, n):
            if graph[x][i] == 'O':
                break
            elif graph[x][i] == 'S':
                return False
    return True

def backtracking(cnt):
    global result
    if cnt == 3:
        if findStudents():
            print('YES')
            exit()
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                backtracking(cnt + 1)
                graph[i][j] = 'X'

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i,j))

backtracking(0)
print('NO')