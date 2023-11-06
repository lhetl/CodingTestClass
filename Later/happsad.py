mes=input().split()
sad=0
happy=0
for i in mes:
    for j in i:
        if j=='S' or j=='A' or j=='D':
            sad+=1
        if j=='H' or j=='A' or j=='P' or j=='Y':
            happy+=1
if happy == 0 and sad==0:
    val=0.5
else:
    val = happy / (sad + happy)
    val = round(val, 4)
print("{:.2f}".format(val*100))