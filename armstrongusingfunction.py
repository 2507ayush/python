def arm(no):
    digit=0
    rev=0
    k=no
    s=no
    while(k>0):
        k=k//10
        digit=digit+1
    while(no!=0):
        ren=no%10
        rev=rev+ren**digit
        no=no//10
    if rev==s :
       print(s)
no=int(input("enter range of numbers = "))
for i in range(0,no):
    arm(i)
