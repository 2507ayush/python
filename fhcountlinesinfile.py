'''with open("pynew.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)'''
f = open("pynew.txt", "r")
x = 0
y = f.read()
z = y.split("\n")
print(z)
for i in z:
    if i:
        x += 1
print("This is the number of lines in the file")
print(x)
