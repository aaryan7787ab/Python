#Electricity Bill calculation
units = int(input("Enter  the consumbed units:"))

if( units <= 100):
    bill = units*2
    print("Your Electricity bill is :",bill,"rs")
elif(  101 < units <= 200):
    bill = units*5
    print("Your Electricity bill is :",bill,"rs")
elif(units < 201):
    bill = units*10
    print("Your Electricity bill is :",bill,"rs")
else:
    print("Your Electricity bill is too much")