y=9
def prime(y) :
    count=0
    for j in range(1,y+1):
        if y%j==0 :
            count=count+1
    if count==2:
        return True
    else :
        return False
print(prime(7))



