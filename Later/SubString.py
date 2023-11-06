num1=31
num2=47
mod1=1e9+9
mod2=1e8+8
h1=0
h2=0
def searchhash(firStr,secStr):
    firlen=len(firStr)
    seclen=len(secStr)
    h1 = 0
    h2 = 0
    length=seclen-firlen+1
    ansCnt=0
    c1=1
    c2=1
    aw1=0
    aw2=0
    for i in range(1,firlen):
        c1=c1*num1%mod1
        c2=c2*num2%mod2
    for i in range(length):
        if(firlen>seclen):
            ansCnt=0
            break
        if i==0:
            for j in range(firlen):
                number = ord(secStr[j])
                number2=ord(firStr[j])
                aw1=(aw1*num1+number2)%mod1
                aw2 = (aw2 * num2 + number2) % mod2
                h1 = (h1 * num1+ number) % mod1
                h2 = (h2 * num2 + number) % mod2
        else:
            firstCharNum=ord(secStr[i-1])
            lastCharNum=ord(secStr[firlen+i-1])
            tmph1=(h1-c1*firstCharNum)%mod1+mod1
            tmph2=(h2-c2*firstCharNum)%mod2+mod2
            h1=(tmph1*num1+lastCharNum)%mod1
            h2=(tmph2*num2+lastCharNum)%mod2
        if aw1==h1 and aw2==h2:
            ansCnt+=1
    return ansCnt

n,p=map(int,input().split())
arr=[]
for i in range(n):
    tstr=input()
    h1=0
    h2=0
    arr.append(tstr)
    # for j in range(len(tstr)):
    #     number = ord(tstr[j])
    #     h1 = (h1 * num1 + number) % mod1
    #     h2 = (h2 * num2 + number) % mod2

    # arr.append((h1,h2))
print(arr)

for i in range(p):
    cnt = 0
    a,b,c=input().split()
    for j in range(int(a)-1,int(b)):
        if c in arr[j]:
            cnt+=1
    print(cnt)

    # tmp='c'.join(arr[int(a)-1:int(b)])
    # print(searchhash(c,tmp))

