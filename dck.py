a=int(input("enter the number"))
count=0
while(a!=0):
    r=a%10
    if (r==0):
        count=1
    a=a//10

    if(count==1):
        print("duck number")
    else :
        print("not duck")
        
    
