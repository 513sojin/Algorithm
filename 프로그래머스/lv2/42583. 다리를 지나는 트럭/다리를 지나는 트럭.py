from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0]*bridge_length)
    truck_bridge = []
            
    while len(queue):
        # 삭제
        if queue[0] != 0:
            truck_bridge.pop(0)
        queue.popleft()

        # 추가
        if truck_weights:
            if sum(truck_bridge) + truck_weights[0] <= weight:
                queue.append(truck_weights[0])
                truck_bridge.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                queue.append(0)
        answer += 1
    return answer 