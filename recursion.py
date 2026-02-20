# Recursion and F-String and Docstring

# Recursion and Docstring
def fact(n=2):
    '''  To find the Factorial of the Number'''
    if(n ==0 or n==1):
        return 1
    else:
        return(n*fact(n-1))

print(fact(4))
print(fact.__doc__)

# F-String
name = input("Enter Your Name: ")
country = input("Enter Your Country Name:")

print(f"Hey my name is {name} \nI am from {country} ")