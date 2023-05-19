f=open("pynew.txt",'r')
y=f.read()
count=0
lst=['a','e','i','o','u']
for i in range(0,len(y)):
    k=y[i]
    if k in lst :
        count = count+1
print("no. of vowels = ",count)

    
