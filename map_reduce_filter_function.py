# Map function...
l = [1,2,5,6,7,9]

def square(a):
    return a*a
# predefined Function as an argument 
newList = list(map(square,l))
print(newList)
# using lambda
newMap  = list(map(lambda x :x * x * x,l))
print(newMap)

# Filter Function...
def filter_func(a):
    return a > 4

newFilter = list(filter(filter_func,l))
print(newFilter)
#Reduce Function ...
from functools import reduce

result = reduce(lambda x,y:x+y,l)
print(result)