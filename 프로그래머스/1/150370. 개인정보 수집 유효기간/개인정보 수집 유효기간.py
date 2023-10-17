def time_convert(t):
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + 28 * month + day


def solution(today, terms, privacies):
    answer = []
    today = time_convert(today)
    month_dict = {}

    for term in terms:
        name, period = term.split()
        month_dict[name] = int(period) * 28

    for idx, privacies in enumerate(privacies):
        dates, name = privacies.split()
        total = time_convert(dates) + month_dict[name]
        if total <= today:
            answer.append(idx + 1)

    answer.sort()
    return answer