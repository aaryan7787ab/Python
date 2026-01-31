# student attendence management system
student = input("Enter the name of the student")
present = int(input("Enter the total presents:"))
workDays = int(input("Enter numbers of working days"))

absents = workDays - present
print(student,"is absent for :",absents,"days")
average = present/workDays*100
print(student,"average attandence is ",average,"%")

if (average < 75):
    print("You should be fined ")
else:
    print("all clear no fine")