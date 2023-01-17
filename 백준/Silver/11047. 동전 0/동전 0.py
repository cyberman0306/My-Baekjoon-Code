n, k = map(int, input().split())
space = []
for i in range(n):
    a = int(input())
    space.append(a)
count = 0
count_money = 0
for i in reversed(space):
    if k <= 0:
        break
    if k >= i:
        temp = (k // i)
        k -= (k // i) * i
        count += temp
        count_money += temp * i
        #print(count)
        #print(count_money)
        #print(k)
 #   else:
 #       print("something wrong")
print(count)