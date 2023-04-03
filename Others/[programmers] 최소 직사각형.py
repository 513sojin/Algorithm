def solution(sizes):
    answer = 0
    w = list()
    h = list()

    for idx, value in enumerate(sizes):
        if sizes[idx][0] < sizes[idx][1]:
            sizes[idx][0], sizes[idx][1] = sizes[idx][1], sizes[idx][0]
        w.append(sizes[idx][0])
        h.append(sizes[idx][1])

    return max(w) * max(h)