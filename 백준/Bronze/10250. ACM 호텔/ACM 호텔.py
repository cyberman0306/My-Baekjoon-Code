hotel = int(input())
for p in range(hotel):
    floor, rooms, n = map(int, input().split())
    guest = 0

    if n // floor == n / floor:
        print(floor * 100 + n // floor)
    else:
        print(n % floor * 100 + n // floor + 1)