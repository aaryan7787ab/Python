#Banking System -- Using OOPs Concept 
class BankAccount:
    def __init__ (self,name,accountNumber,balance):
        self.name=name
        self.accountNumber = accountNumber
        self.balance=balance
        print(f"{name} Your Account Number is {accountNumber} And Current Balance is {balance}")

    def deposite(self,amount):
        self.amount = amount
        self.totalAmount= self.balance+amount
        print(f"Balance is {self.totalAmount}")


    def Withdraw(self,withdraw):
        if(withdraw>self.totalAmount):
            print("Invalid Amount")
        else:
            print(f"Your Withdrawl Amount is {withdraw} \n {self.name} your balance is {self.totalAmount - withdraw}")
    
man=BankAccount("Danial",78990672461688,1000)
man.deposite(500)
man.Withdraw(1200)

