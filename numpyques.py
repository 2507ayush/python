'''
To create a array using numpy for all even numbers from 1 to 100
To create n*n identity matrix where value of n is given by the user
To remove all the numbers in given array which is equal or greater than a given number

from numpy import*
ls=[]
for i in range(0,101):
    if (i%2==0):
        ls.append(i)
print(ls)
a=array(ls)
print(a)



from numpy import*
n=int(input("enter value of n = "))
matrix=[list(range(1+n*i,1+n*(i+1)))for i in range(n)]
print("the created matrix of {} * {}: ".format(n,n))
for m in matrix:
    print(m)

from numpy import*
n=int(input("enter a number = "))
a=identity((n),int)
print(a)
'''
from numpy import*
n=int(input("enter the no. want to remove = "))
ls=[]
for i in range(0,11):
    if (i%2==0):
        ls.append(i)

for j in range(0,len(ls)):
    x=ls[j]
    if(n>=x):
        ls.pop()

a=array(ls)
print(a)








    
