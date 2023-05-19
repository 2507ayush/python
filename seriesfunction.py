def fact(num):
    factorial=1
    if num<0 :
        print("no factorial")
    elif num==0 :
        print("factorial is 1")
    else :
        for i in range(1,num+1):
            factorial = factorial *i

def series(n):
    s=0
    s=s+1/i

n=int(input("enter a number = "))
for i in range(0,n):
    fact(i)
print(series(n))



