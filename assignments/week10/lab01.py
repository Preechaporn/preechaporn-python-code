"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
print("=== PERSONAL INFORMATION VALIDATOR ===")
name = "John Doe"
age = "25"
phone_number = "9876543210"

nameflag = True
for char in name:
    if char.isalpha() == False and char != " ":
        nameflag = False
    if nameflag == False:
        break
    print(char, char.isalpha())

ageflag = True
num = int(age)
if num < 18 and num > 65:
    ageflag = False

phoneflag = True
if len(phone_number) > 10 and len(phone_number) < 1:
    phoneflag == False
else:
    for char in phone_number:
        if char.isdigit() == False and char == " ":
            nameflag = False
        if nameflag == False:
            break
        print(char, char.isdigit())
        
print("\n\nValidation Results:")
if nameflag:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (not contains only letters and spaces)")

if ageflag:
    print(f"Age: Valid ( {num} years old)")
else:
    print("Age: Invalid (less than 18 or more than 65)")

if phoneflag:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (more than 10-digit number)")

print("\n\nFormatted Information:")
print("Name: ",name.upper)
if num >= 18 and num <= 30:
    group = "Young Adult (18-30)"
else:
    group = "Not Young Adult"
print(f"Age Group: {group}")
print(f"Phone: +91-{phone_number}")