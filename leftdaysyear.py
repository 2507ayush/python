d=int(input("enter todays day = "))
m=int(input("enter month number="))
leftdays=0
if (m==1):
    leftdays=leftdays + (365-d)
    print("left days in the year = ",leftdays)
elif (m==2):
    leftdays=leftdays + (334-d)
    print("left days in the year = ",leftdays)
elif (m==3):
    leftdays=leftdays + (306-d)
    print("left days in the year = ",leftdays)
elif (m==4):
    leftdays=leftdays + (275-d)
    print("left days in the year = ",leftdays)
elif (m==5):
    leftdays=leftdays + (245-d)
    print("left days in the year = ",leftdays)
elif (m==6):
    leftdays=leftdays + (214-d)
    print("left days in the year = ",leftdays)
elif (m==7):
    leftdays=leftdays + (184-d)
    print("left days in the year = ",leftdays)
elif (m==8):
    leftdays=leftdays + (153-d)
    print("left days in the year = ",leftdays)
elif (m==9):
    leftdays=leftdays + (122-d)
    print("left days in the year = ",leftdays)
elif (m==10):
    leftdays=leftdays + (92-d)
    print("left days in the year = ",leftdays)
elif (m==11):
    leftdays=leftdays + (61-d)
    print("left days in the year = ",leftdays)
else :
    leftdays=leftdays + (31-d)
    print("left days in the year = ",leftdays)
    

            
