n=int(input())
import sys
sys.setrecursionlimit(10**4)
ans=[0 for i in range(n)]
def dfs(x,y,length,height,array):
    if array[y][x]==0:
        return 0
    array[y][x]=0
    for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
        getX=x+di
        getY=y+dj
        if (0<=getX<length) and (0<=getY<height):
            if array[getY][getX]==1:
                dfs(getX,getY,length,height,array)
    return 1

for i in range(n):
    cnt = 0
    length,height,plantCount=map(int,input().split())
    plantArr =[[] for k in range(plantCount)]
    arr = [[0 for m in range(length)] for n in range(height)]
    for j in range(plantCount):
        arrIndex1, arrIndex2 = map(int, input().split())
        arr[arrIndex2][arrIndex1] = 1
        plantArr[j].append([arrIndex1, arrIndex2])
    for k in plantArr:
        cnt+=dfs(k[0][0],k[0][1], length, height, arr)
    ans[i]=cnt
for i in ans:
    print(i)


