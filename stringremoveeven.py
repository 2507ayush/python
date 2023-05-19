a=input("enter a string = ")
ns=""
for i in range(len(a)) :
    if i%2==1 :
        ns = ns + a[i]
print("even index removed string = ",ns)
