no = int(input("enter a number = "))
rev=0
on = no
while(no!=0):
    r=no%10
    rev=rev*10+r
    no=no//10
print("reverse of the number is = ",rev)

if on==rev :
    print("palindrome number")
else :
    print("not a palindrome number")
    
