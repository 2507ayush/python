ls=[]
x=int(input("enter the no. of elements of list = "))
for i in range(0,x):
    y=int(input("enter  element = "))
    ls.append(y)
print(ls)
for j in range(0,x-1):
    b = ls[j]
    c = ls[j+1]
    f = lambda b,c : b if(b<c)else c
    
    value = f(b,c)
    print(value)


    
