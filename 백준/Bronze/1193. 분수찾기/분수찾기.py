n = int(input())
count = 0
space = 0
i = 0
up = 0
down = 0
line = 0


while n > 0:
    i += 1
    n -= i
    line += 1
n += i

if line % 2 == 0: #짝수, 오른쪽에서 부터 시작
    print(str(n) + "/" + str(i+1-n))
else:
    print(str(i+1-n) + "/" + str(n))
#print("line : ", line)
# print("시부터 ", n, "번째")
##print("해당 라인의 원소 갯수 :", i)

