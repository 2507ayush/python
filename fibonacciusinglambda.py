x=0
y=1
a=int(input("enter length of series = "))
for i in range(0,a):
    f=lambda x,y :x+y
    value=f(x,y)
    print(value)
    x=y
    y=value
    
