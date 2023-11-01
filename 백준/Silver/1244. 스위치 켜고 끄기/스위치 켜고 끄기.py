import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

student = int(input())

def change(i):
    arr[i] = 1 if arr[i] == 0 else 0

for _ in range(student):
    sex, num = map(int, input().split())

    if sex == 1: #남자
        for i in range(num, n + 1, num):
            change(i)

    else: # 여자
        left, right = num, num
        while 2 <= left and right < n and arr[left - 1] == arr[right + 1]:
            left -= 1
            right += 1

        if left == num and right == num:
            change(num)
        else:
            for i in range(left, right+1):
                change(i)

for i in range(1, n+1):
    print(arr[i], end=" ")
    if not i % 20:
        print()