repeatCnt,number=map(int,input().split())
arr=[0 for i in range(repeatCnt)]
def rec(repeat):
    if repeat==0:
        print(arr)
        return
    for i in range(number):
        arr[repeatCnt-repeat]=i
        rec(repeat-1)



if __name__ == "__main__":
    rec(repeatCnt)
