"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program

def personal_info_manager():
    # Create initial person tuple
    personal = ("Preechaporn Jeksoongnoen",19,"Lopburi","Thailand")  # name, age, city, country
    hobbies = []
    i = 1

    while i == 1:
        condition = input("what do you want to do? \n 1 (Display all information)\n 2 (Add new hobbies)\n 3 (Remove hobbies)\n 4 (Update age (by creating a new tuple)\n 5 (Exit)\n : ")
        
        if condition == '1':
            print(f"Name : {personal[0]}")
            print(f"Age : {personal[1]}")
            print(f"City : {personal[2]}")
            print(f"Country : {personal[3]}")
            print(hobbies)
        
        elif condition == '2':
            hobby = input("what is your hobby?\n : ")
            hobbies.append(hobby)

        elif condition == '3':
            hobbies.pop()

        elif condition == '4':
            personal_list = list(personal)
            age = int(input("How old are you"))
            personal_list[1] = age
            personal = tuple(personal_list)

        elif condition == '5':
            i = 0

        else :
            print("enter 1,2,3,4,5")


if __name__ == "__main__":

    personal_info_manager()



