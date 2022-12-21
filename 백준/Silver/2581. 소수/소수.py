
def sosu_maker(n, val):
    space = []
    flag = True

    if val == 1:
        for i in range(2, n + 1): #  n값 포함
            flag = True
            for j in range(2, i):
                if i > j and i % j == 0:
                    flag = False

            if flag is True:
                space.append(i)
        return space
    else:
        for i in range(2, n):
            flag = True
            for j in range(2, i):
                if i > j and i % j == 0:
                    flag = False

            if flag is True:
                space.append(i)
        return space


list_1 = []
list_2 = []

little = int(input())
big = int(input())
list_1 = sosu_maker(little,0)
list_2 = sosu_maker(big,1)

#print(list_1)
#print(list_2)

for i in range(len(list_1)):
    list_2.remove(list_2[0])

#print(list_2)

if len(list_2) == 0:
    print(-1)
else:
    print(sum(list_2))
    print(list_2[0])

