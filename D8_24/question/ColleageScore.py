wScore=[]
kScore=[]
wCnt,kCnt=0,0
for i in range(10):
    wScore.append(int(input()))
for i in range(10):
    kScore.append(int(input()))
for i in range(3):
    wCnt+=max(wScore)
    wScore.remove(max(wScore))
for i in range(3):
    kCnt+=max(kScore)
    kScore.remove(max(kScore))
print(wCnt,kCnt)