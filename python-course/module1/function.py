# Create a function named welcome() that prints:

# def welcome():
#     print("you are my friend")

# welcome()

# Create a function that accepts a student's name and prints:

# def student(name):
#     print(name)

# student("ishaan")

# Create a function that accepts two numbers and returns their product.

# def length(a , b):
#     print(a * b)

# length(5 , 10)

# Create a function with a default argument that prints a city name.

# def place(city = "alwar"):
#     print(city)

# place()

# Create a function named employee() that accepts:

# name
# department

# Call it using keyword arguments.

# def employee(name , department):
#     print(name)
#     print(department)


# employee(department = "IT" , name = "ishaan")

# 1. Create a function that prints your college name.

# def college(name):
#     print(name)

# college("skit")

# 2. Create a function that accepts your name and prints a welcome message.

# def greet(name):
#     print("welcome back" , name)

# greet("ishaan")

# 3. Create a function that accepts two numbers and returns their sum.

# def sum(a , b):
#     return(a + b)

# result = sum(10 , 15)
# print(result)

# 4. Create a function that returns the square of a number.

# n= int(input("enter number:"))

# def square(n):
#     return(n * n)

# result = square(n)
# print(result)

# 5. Create a function with a default argument for country. The default value should be "India".

# def place(country = "INDIA"):
#     print(country)

# place()

# 6. Create a function to calculate the area of a rectangle using parameters.

# def area(length , width):
#     return(length * width)

# result = area(5 , 7)
# print(result)

# 7. Create a function that accepts name, roll_no, and branch, and call it using keyword arguments.

# def employee(name , branch , rollno):
#     print(name)
#     print(branch)
#     print(rollno)


# employee(branch = "IT" , name = "ishaan" , rollno = 5)

# 8. Write a program that uses the built-in functions max(), min(), and sum() on a list of five numbers.

# number = (5 , 4 , 25 , 50)

# print(max(number))
# print(min(number))
# print(sum(number))

# 9. Create a function that returns the larger of two numbers.

# def larger(num1, num2):
#     return max(num1, num2)

# result = larger(5 , 25)
# print(result)

# 10. Create a function that accepts three subject marks, returns the total marks, and prints the average.

# def calculate_marks(subject1, subject2, subject3):
#     total = subject1 + subject2 + subject3
#     average = total / 3
#     print(average)
#     print(total)

# calculate_marks(50 , 60 , 70)

# Create a global variable college and print it inside a function.

# college = "skit"

# def student():
#     global college 
#     college = "ishaan"

# student()
# print(college)

# Create a lambda function to calculate the square of a number.

# number = lambda x : x * x

# print(number(9))

# 1. Create a local variable inside a function and try accessing it outside. What happens?

# def student():
#     name = "ishaan"
#     print(name)
# student()

# 2. Create a global variable and print it inside two different functions.

# information = "name"
# information2 = "age"

# def name():
#     print("ishaan:" , information)

# def age():
#     print("18:" , information2)

# name()
# age()

# 3. Write a lambda function to calculate the cube of a number.

# cube = lambda x: x ** 3
# print(cube(5))

# 4. Write a lambda function to find the larger of two numbers.

# num1 = int(input("enter number:")) 
# num2 = int(input("enter number:")) 

# number = lambda num1 , num2 : num1 >= num2

# if (num1 >= num2):
#     print("large number")
# else:
#     print("small number")