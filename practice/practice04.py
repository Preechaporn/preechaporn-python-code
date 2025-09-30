class BankAccount :
    def __init__(self,accountNumber,name,balance=0):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    def Deposit(self,deposit):
        self.balance += deposit

    def Withdraw(self,withdraw):
        if self.balance < withdraw:
            print(f"can't withdraw!\nyour balance is {self.balance}")
        else:
            self.balance -= withdraw
            
    def bankFees(self):
        return self.balance * 0.05
        
    def Display(self):
        print(f"\nAccount : {self.accountNumber}\nName : {self.name}\nBalance : {self.balance}\nBank Fees : {self.bankFees()}\n")


#main
acc1 = BankAccount("123-456", "Alice", 1000)
acc1.Deposit(500)
acc1.Withdraw(200)
acc1.Display()