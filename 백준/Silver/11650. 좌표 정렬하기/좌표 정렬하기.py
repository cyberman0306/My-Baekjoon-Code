import sys
input = sys.stdin.readline().strip
#.split()
n = int(input())

#n = int(input())

li2 = []
li = [[0 for i in range(2)] for j in range(n)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li[i] = [x, y]
#b = len(li)
#print(b)
# for _ in range(len(li)):
#     a = min(li)
#     li2.append(a)
#     li.remove(a)
li2 = sorted(li)
for i in range(len(li2)):
    print(*li2[i])
