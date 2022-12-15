hotel = int(input())
for p in range(hotel):
    floor, rooms, n = map(int, input().split())
    guest = 0

#    n // h
    if n // floor == n / floor:
        ho = int(n // floor)
        a = format(ho, '02')
        print("%d%s" % (floor, a))
    else:
        dong = (n % floor)
        ho = int(n // floor) + 1
        #print(dong)
        #print(ho)
        ho = format(ho,'02')
        print("%d%s" % (dong, ho))