import math

d,h,w=map(int,input().split())
x=math.sqrt((d*d)/(w*w+h*h))
realh=int(x*h)
realw=int(x*w)
print(realh,realw)