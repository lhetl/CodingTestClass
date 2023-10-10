leaf,des=map(int,input().split())
dest=[1]
arr2=[]
max=0
cnt=0
for i in range(leaf):
    a,b= map(int,input().split())
    if max<a:
        cnt+=a-max
    arr2.append(cnt)
    if (b > max):
        max = b
for i in list(map(int,input().split())):
    dest.append(i)
sum=0
for i in range(len(dest)-1):
    a=dest[i]-1
    b=dest[i+1]-1
    if(a>b):
        tmp=a
        a=b
        b=tmp
    sum+=arr2[b]-arr2[a]
print(sum)