#Lambda Function 

#Ordinary way of writing Function
def cube(x):
    cube = (x*x*x)
    return cube
 
cube(2)

#Lambda 
square = lambda x:x*x
print(square(3))

#Fucntion as an argument 
def solve(fx,value):
    return 6*fx(value)

print(solve(lambda x:x*3,2))