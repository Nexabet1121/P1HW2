
# Nexabet
# 9/26/20240
# P1HW2
# For this assignment you will create a program that does some basic math about expenses
# Ask user for info
print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget: "))
print()
travel_destination = (input("Enter Travel Destination: "))
print()
Gas_expense = int(input("How much do you think you will spend on gas?: "))
print()
accomodation_expense = int(input("Approximately, how much will you need for accomodation/hotel?: "))
print()
food_expense = int(input("Last, how much do you need for food?: "))
Total_expense = int(Gas_expense + accomodation_expense + food_expense)
# Calculate remaining balance
remaining_balance = (budget - Total_expense)

# Display expenses
print()
print("-------------Travel Expenses------------")
print("Location: ", travel_destination)
print("Initial Budget: ", budget)
print()
print("Fuel: ", Gas_expense)
print("Accomodation: ", accomodation_expense)
print("Food: ", food_expense)
print()
print("Remaining Balance: ", remaining_balance)
