#Enumerate Function
r = int(input(" How many number you want to enter : "))
newI = []

for _ in range(r):
    num = int(input("Enter the Numbers:"))
    newI.append(num)
    for index,value in enumerate(newI,start=1):
        print(f"{index} is the value is {value}")

