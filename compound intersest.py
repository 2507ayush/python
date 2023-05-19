'''compound interest'''
p=int(input("enter the principal ="))
r=int(input("enter the rate = "))
t=int(input("enter the time = "))
n = 3
ci = (p*(1+(r/n)))**t
print(ci)
