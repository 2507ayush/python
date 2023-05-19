s=0
count=0
for i in range(100,10000):
    x=i
    k=i
    while(x!=0):
        r=x%10
        count=count+1
        x=x//10
    while(x!=0):
        r=x%10
        s=s+(r**count)
        x=x//10
    if (s==k):
        print(s)
        
        
        
