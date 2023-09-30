hash = {}
visited = [[0]*5 for _ in range(5)]

def bingo():
    count = 0

    for i in range(5):
        row, col = 0, 0
        for j in range(5):
            if visited[i][j]:
                row += 1
            if visited[j][i]:
                col += 1
        if row == 5:
            count += 1
        if col == 5:
            count += 1

    row_diag, col_diag = 0,0
    for i in range(5):
        if visited[i][i]:
            row_diag += 1
        if visited[4-i][i]:
            col_diag += 1
    if row_diag == 5:
        count += 1
    if col_diag == 5:
        count += 1
    return count

num_count = 0
result = 0
for i in range(5):
    l = list(map(int, input().split()))
    for j in range(5):
        hash[l[j]] = (i,j)

for i in range(5):
    l = list(map(int, input().split()))
    for j in range(5):
        num_count += 1
        visited[hash[l[j]][0]][hash[l[j]][1]] = 1

        if bingo() >= 3:
            print(num_count)
            exit()