n=int(input())
arr=[0 for i in range (n)]
arr=list(map(int,input().split()))
arrY=0
arrM=0
for i in range(n):
    arrY+=int(arr[i]/30+1)*10
    arrM+=int(arr[i]/60+1)*15
min=min(arrY,arrM)
if(arrM>=arrY):
    print("Y",end=" ")
if(arrM<=arrY):
    print("M", end=" ")
print(min)