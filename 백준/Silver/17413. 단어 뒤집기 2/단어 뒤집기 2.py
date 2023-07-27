words = list(input())
result = ''
stack = ''

flag = False

for w in words:
    if w == '<':
        flag = True
    elif w == '>':
        flag = False

    if not flag: #괄호 밖
        if w.isalnum(): #뒤집어서 출력
            stack = w + stack
        else: #공백
            stack += w
            result += stack
            stack = ''
    else: #괄호 안
        stack += w
        if w == '>':
            result += stack
            stack = ''

if len(stack) > 0:
    result += stack
print(result)