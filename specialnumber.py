n=int(input("enter a number="))
s=0
f=1
k=1
while n!=0 :
    r=n%10
    while k<=r:
        f=f*k
        k=k+1
    s=s+f
    n=n//10
if s==n :
    print("special number")
else :
    print("not a special number ")
    
print(s)
print(f)
