def checking(a):
    tmpp=True
    leng=len(a)//2
    if len(a)%2==1:
        leng+=1
    for i in range(leng):
        if a[i]!=a[-1*i-1]:
            tmpp=False
    return tmpp
n=input()
m=len(n)
cnt=0
k=0

# 직전 자릿수 까지 계산
for i in range(1,m,2):
    cnt+=2*(pow(10,k)*9)
    k+=1
if m%2==0:
    cnt-=pow(10,k-1)*9
######
if m%2==1:
    k+=1
q=0
#해당 수 -1까지 계산
for i in range(k,1,-1):
    if i==k:
        check=((int)(n[q])-1)
    else:
    # else int(n[m])<int(n[m-1]):
        check=((int)(n[q]))
    # else:
    #     check=((int)(n[m])-1)
    if check<0:
        check=0
    cnt+=(pow(10,i-1)*check)
    q+=1
p=list(n)
for i in range(k-1):
    p[-i-1]=p[i]
cnt2=0
dd=0
if m%2==1:
    dd=len(n)//2+1
else:
    dd=len(n)//2
if m%2==1:
    for i in range((int)(n[dd-1])):
        p[dd-1]=chr(i+48)
        qwe=''.join(p)
        if int(qwe)!=0:

            if int(qwe)<=int(n):
                cnt+=1
elif m%2==0:
    12
    for i in range((int)(max(n[dd-1],n[dd]))):
        p[dd-1]=chr(i+48)
        p[dd]=chr(i+48)
        qwe=''.join(p)
        if int(qwe)!=0:
            if int(qwe)<=int(n):
                cnt+=1

if checking(n):
    cnt+=1
print(cnt)