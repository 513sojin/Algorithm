n = int(input())
temp = []
visited = [0] * n

def backtracking():
    if len(temp) == n:
        print(" ".join(map(str, temp)))
        return

    for i in range(1,n+1):
        if i not in temp:
            temp.append(i)
            backtracking()
            temp.pop()

backtracking()