# This file contain Basic Mathematical Operations 
# Addition 
def add(a,b):
    print(f"Additon is : {a+b}")

#Subtraction
def sub(a,b):
    print(f"Subtraction is : {a-b}")

#Multiplication
def mult(a,b):
    print(f"Multiplication is : {a*b}")

#Division
def div(a,b):
    if(b == 0):
        #Custom error :: 
        raise ValueError("Invalid Input ! ")
    else:
        print(f"Division is :{a/b}")

#Power rule 
def power(a):
    print(f"Square of {a} is : {a**2}")

