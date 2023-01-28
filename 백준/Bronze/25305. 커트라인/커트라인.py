a, b = map(int, input().split())

space = list(map(int, input().split()))

#print(space)

space.sort()
#print(space)
print(space[a-1 - (b-1)])