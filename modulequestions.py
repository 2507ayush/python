'''Q1.wap in python to pick a random character from a given string
Q2.Generate a random password which meet the following condition - 1.password length must be 10 characeter long must contain atleast two upper case letter 1 digit and 1 special character
'''
import random
st=input("enter a string = ")
ls=[]
for i in st:
    ls.append(i)
print(ls)
print(random.choice(ls))

 
      

