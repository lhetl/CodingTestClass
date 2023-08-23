arr=[int(input()) for i in range(5)]
all=0
for i in arr:
    if(i>=40):
        all+=i
    else:
        all+=40
print(int(all/len(arr)))
