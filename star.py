#Create a star pattern 
n = int(input("Enter the value of N :"))
j = 1
if(n <= 0):
    print("Invalid Input!")
else:
    for i in range(j,n+1):
        print(j*"*")
        j+=1
    j = n-1
    for b in range(n-1,0,-1):
            print("*"*b)
            j-=1
