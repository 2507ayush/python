n=int(input())
def Armstrong(n):
    sum=0
    x=n
    while x>0:
        digit=x%10
        sum+=digit**len(str(n))
        x=x//10
    if n==sum:
       return "True"
    else:
       return "false"
out=Armstrong(n)
print(out)
    
    
