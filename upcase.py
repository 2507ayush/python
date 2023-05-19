s=input("enter a string=")
a=len(s)

for i in range(a):
    b=s[i]
    a=ord(b)
    if a>=65 and a<=90 :
        a=a+32
    elif a>=97 and a<=122 :
        a=a-32
    ns=chr(a)
    print(ns,end='')
