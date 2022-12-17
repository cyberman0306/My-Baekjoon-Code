def func(n):
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return n * func(n-1)
a = int(input())
print(func(a))