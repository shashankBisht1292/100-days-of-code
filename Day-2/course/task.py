print(len("Hello"))

#subscripting
print('somil'[-1])

#whole number
print(120+5)

#large number
print(1_200)

#float
print(1.345)

#boolean
print(True)
print(False)

#PAUSE 1. Fix the len() function so it has no more warnings or errors.
len('12345')

#PAUSE 2. Write out 4 type checks to print all 4 data types
print(type("somil"))
print(type(123))
print(type(3.14))
print(type(True))

#Type Conversion
print(int("100") + 50)

#PAUSE 3. Make this line of code run without errors
userName = input("Enter your name")
nameLength = len(userName)
print("Number of letters in your name: " + str(nameLength))

print("My age: " + str(12))
#Learn to use the basic mathematical operators, +, -, *, /, // and **
print(2+4)
print(2*5)
print(5/3)
print(5//3)
print(2**3)

#PAUSE 1. What is the output of this code?
print(3 * 3 + 3 / 3 - 3)

#PAUSE 2. Change the code so it outputs 3?
print(3 * (3 + 3) / 3 - 3)

bmi = 84 / 1.65 ** 2
print(bmi)

#Flooring a Number
print(int(bmi))

#Rounding a Number
print(round(bmi))
print(round(bmi,2))

#Assignment Operators
score = 0
score += 1
print(score)

#f-Strings
print(f"your score is = {score}")
