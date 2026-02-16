# Student Management System 
name = input("Enter the name : ")
classCode = input("Enter your class code")
rollno = int(input("Enter your class Rollno"))
marks1st = int(input("Enter your Marks:"))
marks2nd = int(input("Enter your Marks:"))
marks3rd = int(input("Enter your Marks:"))
marks4th = int(input("Enter your Marks:"))
marks5th = int(input("Enter your  Marks:"))
# System ...
System ={
    "Name ": name,
    "Rollno": (classCode ,rollno),
    "marks": {
        1:marks1st,
        2: marks2nd,
        3: marks3rd,
        4:marks4th,
        5: marks5th,
    }
}
# output
print(System.items())
