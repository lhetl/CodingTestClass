def f(n):
    if n in fib_dict:
        return fib_dict[n]
    if n <= 2:
        return 1
    fib_dict[n] = f(n-1) + f(n-3)
    return fib_dict[n]
fib_dict = {}
n = int(input())
print(f(n-1))