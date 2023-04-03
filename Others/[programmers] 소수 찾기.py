from itertools import permutations


def solution(numbers):
    per = []
    for i in range(1, len(list(numbers)) + 1):
        per += permutations(list(numbers), i)
    arr = [int(("").join(p)) for p in per]

    result = []
    for i in arr:
        if i < 2:
            continue
        isPrime = True  # 소수

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isPrime = False  # 소수 아님

        if isPrime:
            result.append(i)

    return len(set(result))
