# Exception Handling

a = input("Enter the Number: ")
print(f"Multiplication of the Number {a}")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a*i)}")
except:
    print("Invalid Input")

print("Some line of Code ") 
