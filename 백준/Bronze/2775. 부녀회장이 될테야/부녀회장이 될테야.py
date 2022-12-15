n = int(input())

for i in range(n):
    floor = int(input())
    ho = int(input())
    people = [i for i in range(1, ho+1)]

    for j in range(floor):
        sums = []
        for k in range(ho):
            sums.append(sum(people[0:k+1]))
        people = sums.copy()
        #print(people)
    print(people[ho-1])
    #print(people)
