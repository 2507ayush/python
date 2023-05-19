ls=[]
n=int(input("enter no. of elements in a list = "))
for i in range(0,n):
    x=int(input("enter element = "))
    ls.append(x)
print(ls)
def prime(y) :
    return y+y



out=map(prime,ls)
print(list(out))
