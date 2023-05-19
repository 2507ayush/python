def prime(no):
    count=0
    for i in range (1,no+1) :
        if no%i==0:
            count+=1

    if count==2 :
        print("prime number")
    else :
        print("not a prime number")
no=int(input("enter a number = "))
t=prime(no)
print(t)
