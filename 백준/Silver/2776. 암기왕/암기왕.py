import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    first_num = int(input())
    first_arr = set(map(int, input().split()))

    second_num = int(input())
    second_arr = list(map(int, input().split()))

    for num in second_arr:
        if num in first_arr:
            print(1)
        else:
            print(0)