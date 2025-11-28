#foor loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max = student_scores[0]
for score in student_scores:
    if score > max:
        max = score

print(f"The highest score in the list is {max}")

sum = 0
for num in range(1, 101):
    sum += num

print("final is ", sum)

#FizzBuzz
for num in range(1, 101):
    if (num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif (num % 3) == 0:
        print("Fizz")
    elif (num % 5) == 0:
        print("Buzz")
    else:
        print(num)
