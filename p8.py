decrement=8
value=65
increment=64
for i in range(0,5):
    for j in range(0,decrement):
        print(end = " ")
    for k in range(0,i+1):
        increment=increment+1
    value = increment
    temp = value
    for j in range(0,i+1):
        ch=chr(value)
        print(ch ,end=" ")
        value = value-1
    value=temp
    decrement=decrement-2
    print()
    
        
