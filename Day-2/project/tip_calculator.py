print("Welcome to the tip Calculator!")

total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 0r 15?"))
total_people = int(input("How many people to split the bill? "))

final_bill = total_bill+ (total_bill * tip_percentage / 100)
individual_total = round(final_bill /  total_people, 2)

print(f"Each person should pay: ${individual_total}")
