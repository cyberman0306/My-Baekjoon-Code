space = []
set_space = []
n = int(input())
flag = True
total = n
for i in range(n):
    flag = True

    space = list(input())
    #print(space)
    set_space = list(set(space))
    #print(set_space)

    #print()

    for j in range(len(set_space)): # 반복 횟수에는 문제없음
        cnt = space.index(set_space[j]) #  인덱스 추출
        #print("인덱스의 위치: %d" % cnt) # cnt 추출 ok
        #print("해당 철자의 인덱스 갯수")
        #print((space.count(space[cnt]))) #해당 인덱스 철자의 갯수 파악

        for p in range((space.count(space[cnt]))):
            #if space[cnt] is space[cnt+p]:
             #   print("same")
            if space[cnt] is not space[cnt+p]:
                #print("no its not same")
                flag = False
    if flag == False:
        total -= 1
    #print("total is ", total)

print(total)
