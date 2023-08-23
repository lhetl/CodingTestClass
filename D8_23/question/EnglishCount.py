str=input()
arr=[0 for i in range (26)]
for i in str:
    arr[ord(i)-97]+=1
for i in arr:
    print(i,end=" ")
# a=input()
# for c in "abcdefghijklmnopqrstuvwxyz":
#     print(a.count(c),end=" ")