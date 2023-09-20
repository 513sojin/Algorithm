p,m = map(int, input().split())
room = []

for _ in range(p):
    l, n = input().split()

    if not room:
        room.append([(l,n)])
    else:
        flag = False
        for r in room:
            if int(r[0][0]) - 10 <= int(l) <= int(r[0][0]) + 10 and len(r) < m:
                r.append((l,n))
                flag = True
                break

        if not flag:
            room.append([(l,n)])

for r in room:
    r.sort(key= lambda x : (x[1]))
    if len(r) == m:
        print('Started!')
    else:
        print('Waiting!')

    for s in r:
        print(' '.join(map(str, s)))