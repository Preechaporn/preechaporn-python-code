# Exercise 1: Personal Profile Creator
print("=== Personal Profile Creator ===")
# Create a program that asks for:
# - Full name
# - Age
# - Email
# - Phone number
# - Favorite hobby
# Then display it as a profile

# Write your solution here:
while True:
    try:
        option = input("1. What is your name?\n2. How old are you?\n3. What is your email?\n4. What is your phone number?\n5. What is your favorite hobby?\n6. Display your profiles\n7. Exit\noption : ")
        if(option == '1'):
            name = input("enter your name: ")
        elif(option == '2'):
            age = int(input("enter your age: "))
        elif(option == '3'):
            email = input("enter your email: ")
        elif(option == '6'):
            print("name :",name,"age : ",age,"email : ",email)
        elif(option == '7'):
            break
    except ValueError:
        print("Invaid input!!\n please enter number")