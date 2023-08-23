arr= list(map(int,input().split()))
for i in range(len(arr)):
    print(min(arr),end=" ")
    arr.remove(min(arr))