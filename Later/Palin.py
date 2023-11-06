import sys
sys.setrecursionlimit(10**5)
a=input()

def check(count,left,right):
    if left>=right:
        return count
    if a[left]==a[right]:
        return check(count,left+1,right-1)
    else:
        if count >=4:
            return sys.maxsize
        count += 1
#        print(count, left, right)
        return min(check(count,left+1,right),check(count,left,right-1))
ans=check(0,0,len(a)-1)
if(ans <=3):
    print(ans)
else:
    print("-1")