test = ""
test = input()

n = list(test)
#print(test)
#print(n)
# word.index(i) == cro[0] and word.index(i+1) == cro[1] or word.index(i+2) == cro[2]:

"""
 '=' 무조건 크로아티아 알파벳
 '-' 무조건 크로아티아 알파벳
 
"""
space = ['=', '-']
space_2 = ['lj', 'nj', 'dz=']
count = len(n)

for i in range(3):
    if space_2[i] in test:
        #print("@!!!")
        cnt = test.count(space_2[i])
        #print(cnt)
        count -= cnt
        #print(count)



for j in range(len(space)):
    if space[j] in n:
        cnt = n.count((space[j]))
        count -= cnt



print(count)
