def primechecker(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


x = int(input())

for _ in range(x):
    n = int(input())
    a = n // 2
    b = n // 2
    while a > 0:
        if primechecker(a) is True and primechecker(b) is True:
            print(a, b)
            break
        else:
            a -= 1
            b += 1



