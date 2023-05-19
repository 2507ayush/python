'''wap in python to print the pattern of bhurj khalifa
     1
    1 1
   1 0 1
  1 0 0 1
 1 0 0 0 1
1 0 0 0 0 1
hint : use bin() and len()
'''

for i in range(6,0):
    for j in range(1,6):
        if (j<1):
            print(" ")
        elif (j==1|j==6|j==i):
            print("1 ")
        elif (j!=1 & j!=6):
            print("0")
print("\n")
