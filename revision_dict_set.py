# Revision of the topics -- Dictionary and Set 

# Dictionary and its Methods
students = {
    "Name": " Aryan Bhardwaj",
    "Class": "BCA-4TH sem ",
    "Rollno": 24821,
    "subjects": {
        1: " IT and Web",
        2: " Accountancy",
        3: " Visual basics",
        4: " Personal Management",
        5: " System Analysis and Design"
    }
}
# dictionary methods
print(students.keys())
print(students.values())
print(students.items())
print(students["subjects"][1])


# set and its methods
set = { 1, 2, 3,4,5 ,6, " aryan " , " bravo"}

# methods 
print(set.add(0))
print(set.remove(2))
print(set)
print(set.clear())
print(type(set))