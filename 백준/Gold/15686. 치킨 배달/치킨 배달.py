import sys
from collections import deque
import itertools
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
home_queue = deque()
result = []
queue = []

cnt = 0

def chicken_distance(items):
    min_scores = []

    for home in home_queue: #집의 좌표
        min_score = 51
        for chicken in items:  # 치킨 집 좌표
            min_score = min(min_score, abs(chicken[0] - home[0]) + abs(chicken[1] - home[1]))
        min_scores.append(min_score)
    return sum(min_scores)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 집
            home_queue.append((i,j))
        elif graph[i][j] == 2: # 치킨집
            queue.append([i,j])
            cnt += 1

for item in list(itertools.combinations(queue, m)):
    result.append(chicken_distance(item))

print(min(result))