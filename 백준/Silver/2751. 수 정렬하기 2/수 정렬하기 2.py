import sys
input = sys.stdin.readline

n = int(input())
space = []
for i in range(n):
    space.append(int(input()))
space.sort()

for i in range(n):
    print(space[i])