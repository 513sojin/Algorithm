from collections import deque

n,w,l = list(map(int, input().split()))
truck_weights = list(map(int, input().split()))
answer = 0
queue = deque([0] * w)
truck_bridge = []

while len(queue):
    # 삭제
    if queue[0] != 0:
        truck_bridge.pop(0)
    queue.popleft()

    # 추가
    if truck_weights:
        if sum(truck_bridge) + truck_weights[0] <= l:
            queue.append(truck_weights[0])
            truck_bridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            queue.append(0)
    answer += 1

print(answer)