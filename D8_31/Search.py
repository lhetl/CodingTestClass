find=input()
# find=""
# for i in range(100000):
#     find+="a"
k=len(find)

arr=[0 for i in range(26)]
for i in find:
    arr[ord(i)-97]+=1
st=input()
# st=""
# for i in range(200000):
#     st+="a"
M=len(st)
cnt=0

a1=299617
a2=7919
b1=299993
hashList=[]
for i in range(M-k+1):
    ans = [0 for i in range(26)]
    checkStr=st[i:i+k]
    for j in range(k):
        ans[ord(checkStr[j])-97]+=1
    if ans==arr:
        hash1=0
        hash2=0
        for c in checkStr:
            hash1 *= a1
            hash1 += ord(c)
            hash1 %= b1
        if hash1 not in hashList:
            hashList.append(hash1)
            cnt+=1
    print(hashList)
print(cnt)

