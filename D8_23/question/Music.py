sheetMax,timeMax=map(int,input().split())
sheet=[int(input()) for i in range(sheetMax)]
time=[int(input()) for i in range(timeMax)]
max=0
sheetTime=[]
for i in range(len(sheet)):
    for j in range(sheet[i]):
        sheetTime.append(i+1)
for i in time:
    print(sheetTime[i])