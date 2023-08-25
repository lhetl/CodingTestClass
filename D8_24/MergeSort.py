def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid]) #0~mid-1 까지
    right = mergeSort(arr[mid:]) #mid~끝 까지
    
    leftIdx = 0
    rightIdx = 0
    ans = []
    while leftIdx < len(left) and rightIdx < len(right):
    #양쪽에 카드가 남아있다면 작은카드 챙기기
        if left[leftIdx] <= right[rightIdx]:
            ans.append(left[leftIdx])
            leftIdx+=1
        else:
            ans.append(right[rightIdx])
            rightIdx += 1
        ans += left[leftIdx:] #왼쪽 남은카드 이어붙이기
        ans += right[rightIdx:] #오른쪽 남은카드 이어붙이기
    return ans




arr = [9,3,7,2,5,8,9,1,3,7,4,2,8,6,3,8]
arr = mergeSort(arr)
print(arr)

