rows=int(input("enter no. of rows = "))
columns=int(input("enter no. of columns = "))
s=0
M=[[int(input("enter a element = "))for c in range(columns)]for r in range (rows)]
print(M)
for i in range(rows):
    for j in range(columns) :
        if(i==j) :
            s+=M[i][j]
print("sum=",s)


        
    
        
    
