n = int(input())
a = 0
e = []
count = n

if n < 100:
    print(n)
else:
    count = 99
    for i in range(100, n+1): #모든 수를 다 써치
        e = list(map(int, str(i)))
        if e[0] - e[1] == e[1] - e[2]:
            count += 1
    print(count)