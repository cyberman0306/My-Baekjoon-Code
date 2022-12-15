hotel = int(input())
for p in range(hotel):
    floor, rooms, n = map(int, input().split())
    guest = 0

    if n // floor == n / floor:
        ho = int(n // floor)
        print(floor * 100 + ho)
    else:
        dong = (n % floor)
        ho = int(n // floor) + 1
        print(dong * 100 + ho)