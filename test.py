def square(n):
    return n * n



def f(base, exp):
    if exp % 2 == 0:
        if exp <= 1:
            return base * 1
        else:
            return f(base, exp / 2)


print(f(2,6))

