#Condition Check
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry! you have to grow taller before you can ride.")

#PAUSE 1 - What is 10 % 3?
print(10 % 3)

#PAUSE 2 - Check Odd or Even
userInput = int(input("Enter a number: "))

if userInput%2 == 0:
    print(f"{userInput} is an even number")
else:
    print(f"{userInput} is a odd number")

#Nested and elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child ticket is $5.00")
    elif age <= 18:
        bill = 7
        print("youth ticket is $7.00")
    else:
        bill = 12
        print("Adult ticket is $12.00")

    wants_photo = input("Do you want a photo? (y/n)")
    if wants_photo == "y" or wants_photo.lower() == "yes":
        #add $3 to the bill
        bill += 3
    print(f"Your final bill is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

#python pizza
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
else:
    bill += 25
    if pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

#logical operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Free ticket")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
