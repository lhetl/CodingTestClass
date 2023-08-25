arr=[[0,1],[0,2],[0,5],[0,6],[4,3],[5,3],[5,4],[6,4]]
nodeCount=7
lineCount=8
resultArr1=[[0 for j in range(nodeCount)] for i in range(nodeCount)]
#인접행렬
for i in range(nodeCount):
    for j in range(nodeCount):
        dto=[i,j]
        dto2=[j,i]
        if dto in arr or dto2 in arr:
            resultArr1[i][j]=1
for i in resultArr1:
    print(i)
#인접 리스트
resultArr2 = [[]for i in range(nodeCount)]
print("\n\n")
for i in arr:
    resultArr2[i[0]].append(i[1])
    resultArr2[i[1]].append(i[0])
for i in resultArr2:
    print(i)