st="HHHGFGSGSGSDGSHSFHSGFHFAHS"
M=7919
a=5542
hash1=0
hash2=0
find="ABC"
for c in st:
    hash1*=a
    hash1+=ord(c)
    hash1%=M
print(hash1)
b=17
for c in st:
    hash2*=b
    hash2+=ord(c)
    hash2%=M
print(hash2)

