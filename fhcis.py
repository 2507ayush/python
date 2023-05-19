f=open("pynew.txt",'r')
y=f.read()
count=len(y)
lst=['a','e','i','o','u']
for i in range(0,len(y)):
    k=y[i]
    if k in lst :
        count=count-1
        
print("no. of consonants = ",count)

    
