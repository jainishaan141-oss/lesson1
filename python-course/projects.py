# 1. Problem Statement
# Write a program to check whether a password is **Strong** or **Weak**.
# Conditions
# A strong password should:
# - Have at least 8 characters.
# - Contain at least one digit.
# - Contain at least one uppercase letter.

# user = input("enter password:")
# number = int(input("enter number:"))
# char = "A"
# if len(user) == 8:
#     print("correct")
# elif 0 <= number <= 9:
#     print("good")
# elif char.isupper():
#     print("ok")
# else:
#     print("strong password")

# 2. Problem Statement
# Count the number of words in a sentence.
# Logic
# 1. Take a sentence from the user.
# 2. Split the sentence into words.
# 3. Count the words.
# 4. Display the total.

# sentence = input("enter sentence:")
# word = sentence.split()
# word_count = len(word)
# print(f"total number of words: {word_count}")

# 3. If both strings are equal:
# Palindrome
# Otherwise:
# Not a palindrome

# text = "racecar"
# if text == text[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# 4. Store the names and marks of students.
# Display:
# - Student Name
# - Marks
# - Pass/Fail Status
# A student passes if marks are **40 or above**.

# students = [
#     ("Alice", 92),
#     ("Bob", 84),
#     ("john", 65),
#     ("riya", 42),
# ]
# for name, marks in students:
#     if marks >= 90:
#         print("A grade")
#     elif marks >= 75:
#         print("B grade")
#     elif marks >= 50:
#         print("C grade")
#     else:
#         print("fail")
#     print(f"name: {name} | marks : {marks}")

# 5. Create a shopping cart using a nested list.
# Each item stores:
# - Product Name
# - Price
# Display:
# - Product Name
# - Price
# - Total Bill

# products = [
#     ["laptop", 40000],
#     ["mouse", 2000],
#     ["keyboard", 4000]
# ]
# total_bill = 0
# price = products[1] 
# for i in products:
#     print(i[0])
#     print(i[1])
#     print(products,"-",price)
# total_bill += price
# print("total_bill  =",total_bill)

# 6. Problem Statement
# Store the x and y coordinates of different locations using tuples.
# Display each coordinate.
# Logic
# 1. Create tuples for coordinates.
# 2. Store them in a list.
# 3. Use a loop to print each coordinate.

# coordinates = [
#     [1 , 2],
#     [3 , 4],
#     [5 , 6]
# ]
# for point in coordinates:
#     x , y = point
#     print("X =", x, "Y =", y)

# 7. ## Problem Statement
# Store employee details using tuples.
# Each tuple contains:
# - Employee ID
# - Name
# - Department
# Display all employee details.
# Logic
# 1. Create a list of employee tuples.
# 2. Loop through the list.
# 3. Unpack each tuple.
# 4. Print the employee details

# employess = [
#     [501, "ishaan", "IT"],
#     [502, "bob", "CSE"],
#     [503, "john", "ECE"],
#     [504, "riya", "AI"],
#     [505, "roma", "ML"]
# ]
# for employee in employess:
#     emp_id, name, branch = employee
#     print("ID:", emp_id)
#     print("NAME:", name)
#     print("BRANCH:", branch)