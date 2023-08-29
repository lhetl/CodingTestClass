def subSet(left,right,depth):
    if depth==k:
        ans.discard(abs(left - right))
        return
    subSet(left+arr[depth],right,depth+1)

    subSet(left, right+arr[depth], depth+1)

    subSet(left, right, depth+1)
k=int(input())
arr=list(map(int,input().split()))
ans=set()
for i in range(1,sum(arr)+1):
    ans.add(i)
subSet(0,0,0)
print(len(ans))