num = int(input("enter a number = "))
k=num
s=0
while(num!=0):
    r=num%10
    factorial = 1
    for i in range(1,r+1):
        factorial = factorial*i
    s=s+factorial
    num=num//10
if s==k:
    print("no. is peterson number")
else :
    print("no. is not peterson number")

    
