rows=int(input("enter no. of rows = "))
columns=int(input("enter no. of columns = "))
k=0
A=[]
M=[[int(input("enter a element = "))for c in range(columns)]for r in range (rows)]
print(M)
for i in range(rows):
    for j in range(columns) :
        if i>=j :
            k=M[i][j]
            A.append(k)
print(A)

        


        
    
        
    
    
