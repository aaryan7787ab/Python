#Creating a Login System

is_logged_in = True

def login_System(fx):

    def login(*args):
        if (args):
            fx(*args)
            print(f"You are Logged In Successfully")
        else:
            print("You are not logged in")

    return login

            
            
            
@login_System
def name():
    print("This is the Function ")

@login_System
def fulName(name):
    print(f"Hey My Name is {name}") 

name()
fulName("Aryan Bhardwaj")