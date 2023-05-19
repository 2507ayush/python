'''#duck
n=int(input("enter a number = "))
count=0
while n!=0 :
    r=n%10
    if r==0:
        count+=1
    n=n//10
if count>0:
    print("duck number")
else :
    print("not a duck number")
    

#armstrong
n=int(input("enter a number = "))
k=n
g=n
count=0
s=0
while n!=0 :
    r=n%10
    count+=1
    n=n//10
while k!=0 :
    f=k%10
    s+=(f**count)
    k=k//10
if s==g :
    print("armstrong number")
else :
    print("not armstrong ")


#prime number
n=int(input("Enter the number"))
k=n
count=0
for i in range(1,n+1):
    if k%i == 0:
        count+=1
if count==2:
    print("prime ")
else :
    print("not prime")
'''



    
