arr=[i for i in range(30)]
for i in range(28):
    a=int(input())
    arr.remove(a-1)
for i in arr:
    print(i+1)