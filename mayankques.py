ls=[]
ls1=[]
n=int(input("enter no. of elements in a list = "))
for i in range(0,n):
    x=int(input("enter element = "))
    ls.append(x)
print(ls)
def arms(x) :
    digit=0
    rev=0
    k=no
    s=no
    while(k>0):
        k=k//10
        digit=digit+1
    while(no!=0):
        ren=no%10
        rev=rev+ren**digit
        no=no//10
        if rev==s :
            return True
        else :
            return False
    outt=map(arms,out)

def prime(y) :
    count=0
    for i in range(1,y+1):
        if y%i==0:
            count=count+1
    if count==2 :
        return arms()
    else :
        return False
out=map(prime,ls)
print(list(out))
