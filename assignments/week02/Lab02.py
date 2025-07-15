"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
end = 1
while end == 1 :
    condition = input("Do you want to convert THB to USD(type '1') or USD to THB(type '2') : ")
    if condition == "1":
        currency = float(input("how much do you want to converts : "))
        result = currency / 35.5
        print(f"{currency} THB = {result} USD")
        end = 0
    elif condition == "2":
        currency = float(input("how much do you want to converts : "))
        result = currency * 35.5
        print(f"{currency} USD = {result} THB")
        end = 0
    else:
        print("plesae type 1 or 2")
        end = 1
        