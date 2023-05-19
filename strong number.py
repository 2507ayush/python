n=int(input("enter a number - "))
f=1
k=n
s=0
for i in range (1,n+1):
    f=f*i
    s=s+f
if s == k :
    print("strong number")
else :
    print("not a strong number ")
    
