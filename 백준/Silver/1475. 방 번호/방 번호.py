number = input()
dict = {}
temp = 0

for num in number:
    num = int(num)

    if num in dict:
        if num == 9:
            if 6 not in dict:
                dict[6] = 1
                continue
            else:
                if dict[9] > dict[6]:
                    dict[6] += 1
                    continue
        elif num == 6:
            if 9 not in dict:
                dict[9] = 1
                continue
            else:
                if dict[6] > dict[9]:
                    dict[9] += 1
                    continue
        dict[num] += 1
    else:
        dict[num] = 1

print(max(dict.values()))