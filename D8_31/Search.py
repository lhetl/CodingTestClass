from sys import stdin as ss
firStr = str(ss.readline()).strip()
secStr=str(ss.readline()).strip()
firlen=len(firStr)
seclen=len(secStr)
checkArr1=[0]*26
h1=0
h2=0
num1=31
num2=47
mod1=1e9+9
mod2=1e8+8
for i in range(firlen):
    checkArr1[ord(firStr[i])-97]+=1
checkArr2=[0]*26
length=seclen-firlen+1
checkAns=set()
ansCnt=0
c1=1
c2=1
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
            checkArr2[number - 97] += 1
            h1 = (h1 * num1+ number) % mod1
            h2 = (h2 * num2 + number) % mod2
    else:
        firstCharNum=ord(secStr[i-1])
        lastCharNum=ord(secStr[firlen+i-1])
        checkArr2[firstCharNum- 97] -= 1
        checkArr2[lastCharNum - 97] += 1
        tmph1=(h1-c1*firstCharNum)%mod1+mod1
        tmph2=(h2-c2*firstCharNum)%mod2+mod2
        h1=(tmph1*num1+lastCharNum)%mod1
        h2=(tmph2*num2+lastCharNum)%mod2
    check=True
    for k in range(26):
        if checkArr1[k]!=checkArr2[k]:
            check=False
            break
    if check and ((h1,h2) not in checkAns):
        checkAns.add((h1,h2))
        ansCnt+=1
print(ansCnt)
