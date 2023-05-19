def fibonacci(n):
    a=0
    b=1
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return b
    else :
        for i in range(1,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input("enter the terms of fibonacci"))
t=fibonacci(n)
print(t)


