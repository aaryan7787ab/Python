# code for checking the function is a palindrom or not
"""PSEUDO CODE 
1. input from the user 
2. find the length of the name 
3. create a variable with the starting index value(every index starts from 0)
4. create a variable for getting -ve index values.
5. compare them using if statement 
6. increase and decrease the index value ( +- 1 )
7. display the result ..."""

# Code ....

name = input("Enter the Name : ")
length = len(name)
index1 = 0
index2 = length - 1

while index1<index2:
    if(name[index1] != name[index2]):
        print("Not a palindrom")
        break
    else:
        print("Its a palindrom")
    index1 += 1
    index2 -= 1

print("Success ....")