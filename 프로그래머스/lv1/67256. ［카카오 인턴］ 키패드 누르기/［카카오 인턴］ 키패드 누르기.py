def solution(numbers, hand):
    dict = {
        1: [0,0], 2:[0,1], 3:[0,2],
        4: [1,0], 5:[1,1], 6:[1,2],
        7: [2,0], 8:[2,1], 9:[2,2],
        '*':[3,0], 0:[3,1], '#':[3,2]
    }

    left_l = '*'
    right_l = '#'

    left_d = [1, 4, 7]
    right_d = [3,6,9]

    result = ''

    for i in numbers:
        if i in left_d:
            result += 'L'
            left_l = i
        elif i in right_d:
            result += 'R'
            right_l = i
        else:
            left_dict = dict[left_l]
            right_dict = dict[right_l]

            left = abs(dict[i][0] - left_dict[0]) + abs(dict[i][1] - left_dict[1])
            right = abs(dict[i][0] - right_dict[0]) + abs(dict[i][1] - right_dict[1])

            if left < right:
                result += 'L'
                left_l = i
            elif left > right:
                result += 'R'
                right_l = i
            else:
                if hand == 'left':
                    result += 'L'
                    left_l = i
                else:
                    result += 'R'
                    right_l = i

    return result