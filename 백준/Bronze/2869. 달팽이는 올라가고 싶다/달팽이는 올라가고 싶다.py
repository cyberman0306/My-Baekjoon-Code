up, down, tree = map(int, input().split())
snail = 0
day = 0
total = up - down

day = (tree - down) / (up - down)
if day != int(day):
    print(int(day)+1)
else:
    print(int(day))
