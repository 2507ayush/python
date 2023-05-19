def arth(x,y):
    s=x+y
    m=x*y
    d=x//y
    mo=x%y
    p=x**y
    mi=x-y
    di=x/y
    return di,mi,p,mo,d,m,s
x=int(input("enter first number = "))
y=int(input("enter second number = "))
t=arth(x,y)
print(t)
