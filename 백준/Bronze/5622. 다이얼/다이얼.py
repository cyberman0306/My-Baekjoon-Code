letter_space = []
sum = 0
name = list((map(str, input().upper())))
timelist = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
for i in range(26):
    letter_space.append(chr(i+65))
for i in range(len(name)):
    sum += int(timelist[letter_space.index(name[i])])
print(sum)