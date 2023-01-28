z = 0
space = []
for i in range(5):
    a = int(input())
    z += a
    space.append(a)

space.sort()
print("%d" %(z / 5))
print(space[2])

