n = int(input())
space = list(map(int, input().split()))
space_2 = []
flag = True

for i in range(n):
    flag = True
    if space[i] == 1:
        flag = False
    else:
        a = 2
        while a <= space[i]:
            if a == space[i]:
                break
            if space[i] % a == 0:
                flag = False
            a += 1

    if flag is True:
        space_2.append(space[i])

#print(space_2)
print(len(space_2))
