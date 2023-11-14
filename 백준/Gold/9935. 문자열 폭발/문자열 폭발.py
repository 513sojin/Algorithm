import sys
input = sys.stdin.readline
compare = []

stack = input().strip()
bomb = input().strip()

for i in range(len(stack)):
    compare.append(stack[i])
    if ''.join(compare[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            compare.pop()

if compare:
    print(''.join(compare))
else:
    print("FRULA")