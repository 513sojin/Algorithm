def solution(n):
    a = [0] * (n + 1)

    if n < 3:
        return n

    a[1] = 1
    a[2] = 2

    for i in range(3, n + 1):
        a[i] = a[i - 1] + a[i - 2]

    return a[n] % 1234567