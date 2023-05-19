n=int(input())
def Neon(n):
    a=n*n
    c=n
    s=0
    while a!=0:
       d=a%10
       s+=d
       a=a//10
    if s==c:
        return "true"
    else:
        return "false"
out = Neon(n)
print(out)
