def qSort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left = qSort(left)
    right = qSort(right)
    return left + [pivot] + right

arr = [9,3,7,2,5,8,9,1,3,7,4,2,8,6,3,8]
arr = qSort(arr)
print(arr)