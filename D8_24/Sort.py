from functools import cmp_to_key
N = int(input())
arr = []
class Student:
    def __init__(self, age, name, idx):
        self.age = age
        self.name = name
        self.idx = idx
    def __lt__(self, other):
        if other.age == self.age:
            return self.idx < other.idx
        return self.age < other.age
def comp(a,b):
    if a[0] != b[0]:
        if a[0]>b[0]:
            return 1
    return -1
    if a[1] > b[1]:
        return 1
    if a[1] == b[1]:
        return 0
    return -1

for i in range(N):
    age,name = input().split()
    age = int(age)
    arr.append([age,i,name])

arr = sorted(arr,key=cmp_to_key(comp))
for v in arr:
    print(v[0],v[2])