x=0
y=1
count=0
n=int(input("enter the length of fibonacci series  = "))
if n<0 :
    print("fibonacci not possible ")
elif n==0 :
    print(x)
else :
    while count < n :
        print(x,end=' ')
        z=x+y
        x=y
        y=z
        count=count+1
    
