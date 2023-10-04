testCnt=int(input())
arr=[]

for i in range(testCnt):
    arr.append(int(input()))
maxVal=max(arr)
prime=[0 for i in range(maxVal)]
for i in range(2,maxVal):
    if (i*i>=maxVal):
        break
    if prime[i-1]==0: #만약 소수면
        for k in range(i*i,maxVal+1,i):
            prime[k-1]=1
ans=[0]*2
for j in range(testCnt):
    maxN=arr[j]
    mid=arr[j]//2
    for i in range(2,mid+1):
        if prime[i-1]==0:
            if prime[maxN-i-1]==0:
                ans=[i,maxN-i]
    for i in ans:
        print(i,end=" ")
    print()