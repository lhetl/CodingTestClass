import sys

person,objectPrice,sellPrice=map(int,input().split())
if(objectPrice>=sellPrice):
    print("-1")
    sys.exit()
cnt=0
minus=sellPrice-objectPrice
print(person//minus+1)