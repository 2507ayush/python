no = int(input("enter a number = "))
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
    print("armstrong number")
else :
    print("not a armstromg number")
    
