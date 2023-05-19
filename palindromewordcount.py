str="My mom and dad appointed an madam to teach us"
k=str.split()
print(k)
l=len(k)
ls=[]
count=0
for i in range(l) :
    x=k[i]
    y=x[::-1]
    if x==y :
        count=count+1
print("palindrome words in sentence are  =",count)


