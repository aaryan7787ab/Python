# Question and Answer Game ...
question = ("Who is the prime minister of India" ,
           " 1. Narander modi",
           " 2.Amit shah ",
           "3. trump " ,
           "4. None of the above")

for q in question:
    print(q)

try:
    i = int(input("Enter the option Number"))

    if(i == 1):
        print("Your Anser is Correct")
    elif(1 < i <= 4):
        print(" ooo you Lost!")
    else:
        print("Invalid Input")

except ValueError:
    print("You Choose the Invalid Option")
