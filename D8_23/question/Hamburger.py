import sys

arr=[int(input()) for i in range(5)]
# v1=min(arr[0:2])
# v2=min(arr[3:5])
# print(v1+v2-50)
min=sys.maxsize
for i in range(3):
    for j in range(3,5,1):
        if(arr[i]+arr[j]<min):
            min=arr[i]+arr[j]
print(min-50)