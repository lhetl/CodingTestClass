start,end=map(int,input().split())

for j in range(start,end+1):
    check=True
    for i in range(2,int(j**0.5)+1,1):
        if j%i==0:
            check=False
            break
    if check==True and j!=1:
        print(j)