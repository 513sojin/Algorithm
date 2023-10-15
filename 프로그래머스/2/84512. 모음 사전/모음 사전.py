temp = []
alp = ['A', 'E', 'I', 'O', 'U']

num = 0

def bfs(word):
    global num

    tmp_word = ''.join(map(str, temp))
    if word == tmp_word:
        return num
    if len(temp) == 5:
        return

    for a in alp:
        num += 1
        temp.append(a)
        if bfs(word):
            return num
        temp.pop()


def solution(word):
    bfs(word)
    return num