number8=input()
if(number8[0]=='0'):
    number8=number8[1:]
number2=""
for i in number8:
    print(format(int(i),'03b'),end="")
    # number2 += format(int(i), '03b')
# if(number2[0]=='0'):
#     number2=number2[1:]
# print(number2)


