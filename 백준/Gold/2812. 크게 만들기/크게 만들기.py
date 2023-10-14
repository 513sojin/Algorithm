n, temp = map(int, input().split())
nums = list(map(str, input().strip()))

stack = []
k = temp

for num in nums:
    while stack and stack[-1] < num and k > 0:
        k -= 1
        stack.pop()
    stack.append(num)

print(''.join(map(str, stack[:n-temp])))