def arms(x):
    count=0
    s=0
    while(x!=0):
        r=x%10
        count+=1
        x=x//10
    while(x!=0):
        y=x%10
        s=s+(y*y*y)
        x=x//10
    print("armstrong prime number")
        

n=int(input("enter a number = "))
count=0
k=n
for i in range(1,n+1) :
    if(n%i==0):
        count+=1
if(count==2):
    goto arms(n)
else :
    print("not a prime number")
    
