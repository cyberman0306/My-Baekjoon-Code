h, w = map(int, input().split())
li = list(map(int, input().split()))
answer = 0

for i in range(1, w - 1):
    leftMax = max(li[:i])
    rightMax = max(li[i+1:])
    stdValue = min(leftMax, rightMax)
    if li[i] <= stdValue:
        answer += stdValue - li[i]

print(answer)