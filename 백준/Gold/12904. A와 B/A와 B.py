import sys
input = sys.stdin.readline

s = list(input().strip())
t = list(input().strip())

while t:
    if t[-1] == 'B':
        t.pop()
        t.reverse()
    elif t[-1] == 'A':
        t.pop()

    if s == t:
        print(1)
        exit()

print(0)