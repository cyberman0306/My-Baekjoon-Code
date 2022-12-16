n = int(input())
a = True
three = 0
while n >= 0:
    if n % 5 == 0:
        print(three + n//5)
        break
    else:
        three += 1
        n -= 3

if n < 0:
    print(-1)