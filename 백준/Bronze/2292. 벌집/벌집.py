n = int(input())
level = 1
step = 1


while level < n:
    level += step * 6
    step += 1
    #print(level)
    #print(step)

#print()
#print(level)
print(step)