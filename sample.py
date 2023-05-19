for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=' ')
            i=i+1
            j=j+1
    print()
    
