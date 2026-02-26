#Create a class to store the basic details about the student.

class Student:
    def __init__(self,name,age,course,year):#__init__ is a keyword used for creating a constructor
        self.name=name
        self.age = age
        self.course = course
        self.year=year
        print(f" Hey !! I am {name}\n I am {age} years old\n I am in {course} started in {year} ")     


rahul = Student("Rahul",19,"BCA-4th Semester",2024)

