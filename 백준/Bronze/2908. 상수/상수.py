a, b = input().split()
space_a = ""
space_b = ""
for i in a:
    space_a = i + space_a

for i in b:
    space_b = i + space_b

#print(space_a)
#print(space_b)

if int(space_a) > int(space_b):
    print(space_a)
else:
    print(space_b)