def f(n):
    if n in fib_dict:
        return fib_dict[n]
    if n <= 1:
        return n
    fib_dict[n] = f(n-1) + f(n-2)
    return fib_dict[n]
fib_dict = {}
n = int(input())
print(f(n))
#반복형
fib = [0,1,1]
n = int(input())
for i in range(1,n+1):
    fib.append(fib[-1]+fib[-2])
print(fib[n])