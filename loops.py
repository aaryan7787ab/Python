# match case and loops -- for loop and while loop
# Match case statement 

name = input("Enter your name : ")
match name:
    case _ if (name == "Aryan"):
        print(name,"This is your name :")
    case  _:
        print("You are not my owner")

# for loop

for i in name :
    print(i)

# for loop with range keyword

for i in range (2,20,4):
    print(i)

# Do while loop in Python 

while True:
    number = int(input("Enter the value : "))
    print(number)
    if( number >= 10):
        break
print("This is Do while loop in python ")

# While loop 

num = int (input("Enter the value of Number"))
i = 0
while ( num <= 15):
    print(num , "x",i+1,"=",num*(i+1))
    i+= 1
    if(i == 10):
        break
print("Loop is end ")