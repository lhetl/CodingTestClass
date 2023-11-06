from sys import stdin
n=int(stdin.readline().strip())
arr=list(map(int,stdin.readline().strip().split()))
avg=[]
val=sum(arr)
if val%n==0:
    avg.append(val//n)
else:
    avg.append(val//n)
    avg.append(avg[0]+1)
arr.sort()
arr.reverse()
cnt=0
tmp=0
for i in range(n):
    if arr[i]>avg[-1]:
        cnt+=arr[i]-avg[-1]
        tmp+=arr[i]-avg[-1]
    elif arr[i]<avg[0]:
        if tmp>=avg[0]-arr[i]:
            tmp-=avg[0]-arr[i]
        else:
            for j in range(i-1,-1,-1):
                if tmp >= avg[0] - arr[i]:
                    tmp-=avg[0] - arr[i]
                    break
                elif arr[j]>=avg[0]:
                    cnt+=1
                    tmp+=1
print(cnt)