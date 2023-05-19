n=int(input("enter a number = "))
def palindrome(n):
    k=n
    rev=0
    while n!=0:
        r=n%10
        rev = rev*10+r
        n=n//10
    if rev == k :
        return True
    else :
        return False
out = palindrome(79)
print(out)
