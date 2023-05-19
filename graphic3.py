from turtle import*


def r(x,y):
    rt(x)
    fd(y)


tracer(4)
fd(100)
bgcolor("black")
color("cyan")
width(3)

for i in range(1000):
    fd(i)
    r(i,90)
    r(i,90)
    r(i,270)
    r(i,90)
    circle(100,90)


done()
