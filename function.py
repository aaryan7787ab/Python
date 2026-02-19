# Here is the topic -- Function
def calculate(a ,b ):
    mean = (a*b)/(a+b)
    print(mean)

calculate(89,90)


# Functions Arguments

#Default Arguments in function 
def sum ( a =0, b = 0):
    return (a+b)

#Keyword Argument in function 

def name(fname,lname):
    print("Hello",fname,lname)

name(lname="Bhardwaj",fname="Aryan")

#Required Argument in function 
def mult( a , b):
    print(a*b)# a and b are required arguments we have to pass a value to the argument to run function

mult(9,7)

# Variable-Length Argument in function 
def fulnames(*name):
    print(type(name))
    print("Hello",name)

fulnames("aryan", "jiya","harry","guru","davil")

