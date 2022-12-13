n = input()
word = list(map(str, n.split(" ")))
#print(n)
#print(word)

while '' in word:
    if '' in word:
        del word[word.index('')]

print(int(len(word)))