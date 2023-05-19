ls=[]
x=int(input("enter number of elements of list = "))
for i in range(0,x):
    y=int(input("enter elements of a list = "))
    ls.append(y)
print(ls)
for j in range(0,x):
    b = lambda z:z*z
    z=ls[j]
    value=b(z)
    print("square of elements = ",value)
    
for k in range(0,x):
    l=lambda o:o*o*o
    o=ls[k]
    value1=l(o)
    print("cube of elements = ",value1)

