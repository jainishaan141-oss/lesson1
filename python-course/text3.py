# i recived 37/40 in test 3
# ---------------------------------------------------------------------------------------------------

# Section A – Multiple Choice Questions (10 × 1 = 10 Marks)
# Choose the correct option.

# Q1.
# Which keyword is used to create a function in Python? -- c(def)

# A. function
# B. create
# C. def
# D. fun

# Q2.
# What is the output?
# defgreet():print("Hello")greet() -- a(hello)

# A.
# Hello
# B.
# greet
# C.
# Error
# D. Nothing

# Q3.
# What are the values passed while calling a function called? -- c(arguments)

# A. Parameters
# B. Variables
# C. Arguments
# D. Identifiers

# Q4.
# Which statement returns a value from a function? -- d(return)

# A. print
# B. break
# C. continue
# D. return

# Q5.
# Which argument is used when the parameter name is specified during the function call? -- c(default argument)

# A. Positional Argument
# B. Keyword Argument
# C. Default Argument
# D. Local Argument

# Q6.
# Which of the following creates a string? -- a(name = "python")

# A.
# name="Python"
# B.
# name= [Python]
# C.
# name= {Python}
# D.
# name= (Python)

# Q7.
# What is the output?
# word="Python"print(word[2]) -- c(t)

# A. P
# B. y
# C. t
# D. h

# Q8.
# Which method converts all letters to uppercase? -- b(upper())

# A. lower()
# B. upper()
# C. replace()
# D. split()

# Q9.
# Which method is used to split a sentence into words? -- c(split())

# A. strip()
# B. join()
# C. split()
# D. replace()

# Q10.
# Which loop is commonly used to visit every character in a string? -- b(for)

# A. while
# B. for
# C. if
# D. switch

# Section B – Find and Fix the Errors (5 × 2 = 10 Marks)
# Correct the errors in the following programs.

# Q1.
# Defgreet():print("Hello")greet()

# def greet():
#     print("hello")
# greet()

# Q2.
# defadd(a b):returna+bprint(add(10,20))

# def add(a , b):
#     return a+b
# add(10, 20)
# print(add)

# Q3. X
# name="Python"print(name[6])

# name = "python"
# print(name[0 : 6])

# Q4.
# text="hello"print(text.upper)

# text = "hello"
# print(text.upper())

# Q5.
# defdisplay():message="Welcome"print(message)

# def display():
#     message = "welcome"
# print(display)

# Section C – Theory Questions (5 × 2 = 10 Marks)

# Q1.
# What is a function? Write any two advantages of using functions.

# instead of writing same thing again and again , we write inside function and call it when we use
# reduce code 
# make program easier to read

# Q2.
# What is the difference between parameters and arguments?

# parameters --> variable written inside function definition they receive values when we call it
# arguments --> actual values passed to function when we call it

# Q3.
# Differentiate between local variables and global variables with one example each.

# local --> def student():
                    #  name = "rahul"
                    #  print(name)
        #   student()
# global --> name = "ishaan"
        #    def display():
        #              print(name)
        #    display()
        #    print(name)

# Q4. X
# What is string slicing? Explain with one example.

# string slicing --> extract part of string
# example --> name = "ishaan"
#             print(name[0 : 2])
#             print(name[:: 6])

# Q5.
# Write the purpose of any four string methods from the following:
# - upper()
# - lower()
# - replace()
# - split()
# - join()
# - strip()


# 1. upper --> convert all lowercase letters to uppercase
# name = "xyz"
# print(name.upper())

# 2. lower --> convert all uppercase letters to lowercase
# name = "XYZ"
# print(name.lower())

# 3. replace --> replace one substring with another
# sentence = "i love cars"
# print(sentence.replace("cars", "watches"))

# 4. split --> splits string into list
# sentence = "i love cars"
# print(sentence.split())


# Section D – Coding Questions (5 × 2 = 10 Marks)

# Q1.
# Write a function named `square()` that accepts a number as a parameter and returns its square.
# Example Output:
# Square = 49

# def square(num):
#     return num * num
# result = square(7)
# print(result)

#Q2.
# Write a Python program to count the number of vowels in a string entered by the user using a **for loop**.
# Example:
# Input:
# Programming
# Output:
# Vowels = 3

# word = input("enter word:")
# count = 0
# for chin in word:
#     if chin in "aeiouAEIOU":
#       count += 1
# print(count)

# Q3.
# Write a Python function `greet()` that uses a **default argument** `"Student"`.
# Example Output:
# Welcome Student
# Welcome Rahul

# def greet(name = "student"):
#     print("welcome", name)
# greet()
# greet("rahul")

# Q4.
# Write a Python program that:
# - Takes a string as input.
# - Prints it in uppercase.
# - Prints it in lowercase.
# - Prints the total number of characters.
# Example:
# Input:
# Python
# Output:
# PYTHON
# python
# Length = 6

# user = input("enter string:")
# print(user.upper())
# print(user.lower())
# length = len(user)
# print(length)

# Q5.
# Write a Python program to check whether the word `"Python"` exists in a sentence entered by the user.
# Example:
# Input:
# I am learning Python Programming
# Output:
# Python Found

# text = "I am learning Python Programming"
# print(text.find("Python"))