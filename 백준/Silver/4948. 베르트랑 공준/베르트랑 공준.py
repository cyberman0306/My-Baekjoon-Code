
while True:
    a = int(input())
    if a == 0:
        break
    count = 0
    answer = []
    # start, end = map(int, input().split())
    start, end = a + 1, a * 2
    space = [False, False] + [True] * (end - 1) # 공간 전체 초기화, 0, 1은 소수일수없으니 바로 False

    for i in range(2, end + 1):
        if space[i] is True:
            answer.append(i)
            for j in range(2 * i, end + 1, i):
                space[j] = False # 소수 하나를 answer에 넣고 그 소수의 배수는 전부 False로 처리

    for i in range(len(answer)):
        if answer[i] > end:
            break
        if answer[i] >= start:
            #print(answer[i])
            count += 1
    print(count)
