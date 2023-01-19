n = int(input())
space = []
for i in range(n):
    space.append(int(input()))


space = sorted(space)

for i in range(len(space)):
    print(space[i])

