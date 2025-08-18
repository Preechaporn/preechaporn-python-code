"""
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Full name: {first_name *2} {last_name *2}")
"""

"""
my_string = "Hello Python"
my_integer = 42
my_float = 3.14
my_boolean = False
print("Type of my_string:", type(my_string))
print("Type of my_integer:", type(my_integer))
print("Type of my_float:", type(my_float))
print("Type of my_boolean:", type(my_boolean))
"""

"""
fruits = ["apple", "banana", "orange"]

fruits[0:2] = ["pear", "cherry"]
print(fruits)  # ['pear', 'cherry', 'orange']

removed_fruit = fruits.pop()     # Remove and return last element
print(f"Removed: {removed_fruit}")  # apple
print(fruits)  # ['pear', 'cherry', 'orange', 'grape', 'kiwi']
"""

"""
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96, "Eve": 89}

print(f"Number of students: {len(scores)}")
print(f"Is Alice in scores? {scores["Alice"]}")
print(f"Is 'Frank' in scores? {'Frank' in scores}")
"""

subjects = ["Math", "Science", "English"]
default_scores = dict.fromkeys(subjects, 0)
print(f"Default scores: {default_scores}")