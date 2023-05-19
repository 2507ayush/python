from turtle import*


def r(x,y):
    rt(x)
    fd(y)


tracer(4)
fd(100)
bgcolor("black")
color("cyan")
width(3)

for i in range(2003):
    fd(i)
    r(150,i)
    r(150,i)
    r(270,i)
    r(150,i)
    circle(100,90)


done()
