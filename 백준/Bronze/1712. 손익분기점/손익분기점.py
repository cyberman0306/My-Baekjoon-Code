a, b, c = map(int, input().split())
x = 0
if b >= c:
    print(-1)

else:
    print(int(a / (c-b))+1)