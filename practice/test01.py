monthly_income = float(input("User's monthly income in THB : "))
rent_cost = float(input("Monthly rent/housing cost : "))
food_budget = int(input("Monthly food budget in THB : "))
transportation_cost = float(input("Monthly transportation expense : "))
entertainment_budget = int(input("Monthly entertainment budget : "))
emergency_fund_percent = float(input("Percentage to save for emergency : "))
investment_percent = float(input("Percentage to invest (e.g. , 15.0) : "))

Total_Fixed_Expenses = rent_cost + transportation_cost
Total_Variable_Expenses = food_budget + entertainment_budget

Total_Expense = Total_Fixed_Expenses + Total_Variable_Expenses
Remaining_Income = monthly_income - Total_Expense
Emergency_Fund_Amount = monthly_income * (emergency_fund_percent / 100)
Investment_Amount = monthly_income * (investment_percent / 100)
Available_for_Savings = Remaining_Income - Emergency_Fund_Amount - Investment_Amount
Expense_Ratio = (Total_Expense / monthly_income) * 100

print("\n\n\n=== MONTHLY BUDGET REPORT ===\n")
print(f"Income: {monthly_income} THB\n")
print(f"Fixed Expenses: {Total_Fixed_Expenses} THB\n")
print(f"Variable Expense: {Total_Variable_Expenses} THB\n")
print(f"Total Expense: {Total_Expense} THB\n")
print(f"Remaining: {Remaining_Income} THB\n")

print("=== SAVINGS BREAKDOWN ===\n")
print(f"Emergency Fund({emergency_fund_percent}%): {Emergency_Fund_Amount} THB\n")
print(f"Investment({investment_percent}%): {Investment_Amount} THB\n")
print(f"Available for Saving: {Available_for_Savings} THB\n")

print("=== ANALYSIS ===")
print(f"Expense Ratio: {Expense_Ratio}%")