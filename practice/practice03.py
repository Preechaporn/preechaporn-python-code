balance = 0
def Deposit():
    global balance
    deposit = int(input("how much do you want to deposite : "))
    balance += deposit
    print("deposite is success")

def Withdraw():
    global balance
    while True:
        withdraw = int(input("how much do you want to withdraw : "))
        if withdraw >= balance:
            print(f"can't withdraw.\nyou don't have monney enought ({balance})\n")
        else:
            balance -= withdraw
            break
    
def show_balance():
    global balance
    print(f"your monney : {balance} Bath")

if __name__ == "__main__" :
    while True:
        choice = input("\n1. Deposit\n2. Withdraw\n3. Show balance\n4. Exit\n :")
        if choice == '1':
            Deposit()
        elif choice == '2':
            Withdraw()
        elif choice == '3':
            show_balance()
        elif choice == '4':
            break
        else:
            print("invaid value please enter 1-4")
