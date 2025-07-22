'''
# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")
'''

balance = 1000
pin = "1234"
i = 1

while i == 1:
    entered_pin = input("Enter PIN: ")
    if entered_pin == pin:
        i = 0
        print("PIN accepted")
        while True:
            print("\n1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit") 
            print("4. Exit")
        
            choice = input("Choose option: ")
            if (choice == '1'):
                print(f"Your balance is : {balance}")
            elif (choice == '3'):
                while True:
                    try:
                        deposit = float(input("How much do you want to deposit : "))
                        if deposit <= 0:
                            print("Please enter a number greater than 0.")
                        else:
                            balance += deposit
                            print("Deposit is successful.")
                            break
                    except ValueError:
                        print("Invalid input! Please enter a number.")

            elif (choice == '2'):
                while True:
                    try:
                        withdraw = float(input("How much do you want to withdraw : "))
                        if withdraw > balance and withdraw > 0:
                             print("Can't withdraw. Your money isn't enough!!!")
                        elif withdraw <= 0:
                            print("Please enter a number greater than 0.")
                        else:
                            balance -= withdraw
                            print("Withdraw is successful.")
                            break
                    except ValueError:
                        print("Invalid input! Please enter a number.")

            elif (choice == '4'):
                break
            else :
                print("what are you enter!!!\nplease enter 1-4!!!")
            
    else :
        print("password is incorrect!!")