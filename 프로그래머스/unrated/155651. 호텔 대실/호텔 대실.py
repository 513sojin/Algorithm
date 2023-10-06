import sys
def change_time(time):
    h, m = time.split(':')
    return int(h)*60 + int(m)

def solution(book_time):
    book_time = [(change_time(b[0]), change_time(b[1])) for b in book_time]
    book_time.sort(key = lambda x: x[0])
    
    result = []
    INF = sys.maxsize
    
    for b in book_time:
        if result:
            change_idx = INF
            diff = INF
            
            for idx, r in enumerate(result):
                if r <= b[0] and diff >= (b[0]-r):
                    change_idx = idx
                    diff = b[0] - r
            
            if change_idx != INF:
                result[change_idx] = b[1]+10
                continue
            
        result.append(b[1]+10)
        
    return len(result)