# list and tuple -- revision 

# list is a collection of various datatypes -- int , float , string , Boolean
array = [1,2,3,89.89,"Aryan Bhardwaj " , " 67Car-Area",True]
# List and its methods
print(type(array))
print(len(array))

array.append(9) # append value at the end 
print(array)

array.insert(1,90)
array.insert(5,9)# insert 9 at the index value of 5 
print(array)

array.remove(9)# first occurance of the value so -- 5th index -- 9 ---- remove 
print(array)
array.pop(6)# it will remove the 9 which is at the place of 11
print(array)

array2 = [1,6,7,9,45,0,3,4,78,54,3445]
print(array2)
array.reverse()# reverse operation on the list 
print(array)
array2.sort()# note that sorting is run successfully onthe int and float values not -- string ,boolean and none value 
print(array2)
array2.sort(reverse=True)# descending order values 
print(array2)

# tuple -- immutable values 

tuple = (8,9,6,5,"Aryan",9,9,9,9)
print(len(tuple))# length of the tuple 
print(tuple.index(9))# index value of the element 
print(tuple.count(9))# count the occurance of the element .. 

