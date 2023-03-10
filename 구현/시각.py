# 시각
n = int(input())
count = 0
time = ''

for h in range(n + 1):
    time = ''
    if h < 10:
        time = '0' + str(h)
    else:
        time += str(h)

    for m in range(60):
        if m < 10:
            time = time[:2] + '0' + str(m)
        else:
            time = time[:2] + str(m)

        for s in range(60):
            if s < 10:
                time = time[:4] + '0' + str(s)
            else:
                time = time[:4] + str(s)

            if '3' in time:
                count += 1

print(count)

# 책 답안
# for h in range(n + 1):
#     for m in range(60):
#         for s in range(60):
#             if '3' in str(h)+str(m)+str(s):
#                 count += 1

# 정리
# 어차피 3이 들어가기만 하면 되는거라 위의 코드처럼 간단하게 쓰는게 매우 좋아보인다.