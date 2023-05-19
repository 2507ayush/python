n = int(input("enter a number = "))
ns=n*n
s=0
while ns!=0 :
    r=ns%10
    s=s+r
    ns=ns//10
if s==n :
    print("neon number")
else :
    print("not a neon number")
    
