l=[]
rows=int(input("enter the no. of rows"))
cols=int(input("enter the no. of columns"))
for i in range(rows):
    a=[]
    for j in range(cols):
        x=int(input())
        a.append(x)
    l.append(a)
print(l)
