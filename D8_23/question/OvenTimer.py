time,min = map(int,input().split())
plusMin=int(input())
time+=int(plusMin/60)
min+=plusMin%60
if(min>=60):
    min-=60
    time+=1
if(time>=24):
    time-=24
print(time,min)