"""Task: Create a secure bank account system.
Class Name: BankAccount
Attributes: account_holder, balance.
Methods:
deposit(amount): Adds money to the balance.
withdraw(amount): Subtracts money only if balance >= amount. If not, print "Insufficient Funds!".
check_balance(): Prints the current balance."""

class BankAccount:
    def __init__(self):
        self.accountHolder=""
        self.balance=0
        
    def inputs(self):
        self.accountHolder=input("Account Holder Name: ")
        self.balance=int(input("Account Balance: "))
    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        if amount>self.balance:
            print("ERROR: Insufficient Funds")
            
        else:
            self.balance-=amount
            
    def checkBalance(self):
        print(f"You Have {self.balance}$ In Your Account")
        
holder1=BankAccount()
holder1.inputs()
holder1.deposit(int(input("Input Amount You Want To Deposit: ")))
holder1.withdraw(int(input("Input Amount You Want To Withdraw: ")))
holder1.checkBalance()