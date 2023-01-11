n, m = map(int, input().split())

space = []
space2 = []
space3 = []
space4 = []

for i in range(n):
    a = []
    a = input().split()
    a = list(a)
    #print(a)
    space.append(a)
    #print(space)

for i in range(n):
    a = []
    a = input().split()
    a = list(a)
    #print(a)
    space2.append(a)

for i in range(n):
    space3 = []
    for j in range(m):
        space3.append(int(space[i][j]) + int(space2[i][j]))
    space4.append(space3)

for i in range(len(space4)):
    print(*space4[i])