import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
space = []
for i in range(n):
    space.append(int(input()))

#print(space)
space.sort()

# for i in space:
#     space3[space2.index(i)] += 1
#     print(space3)
listCount = Counter(space).most_common()

print(round(sum(space)/n))
print(space[n//2])
if len(listCount) > 1 and listCount[0][1] == listCount[1][1]:
    print(listCount[1][0])
else:
    print(listCount[0][0])
print(max(space) - min(space))