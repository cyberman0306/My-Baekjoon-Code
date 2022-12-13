n = input().upper()
word_list = list(set(n))

#count = []
count_space = []

for i in word_list:
    count = n.count(i)
    count_space.append(count)
    #print(count_space)
    #print(i)

if count_space.count(max(count_space)) > 1:
    print("?")
else:
    #print(count_space.index(max(count_space)))
    print(word_list[count_space.index(max(count_space))])