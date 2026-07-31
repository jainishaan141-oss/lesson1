# Create a list of five fruits and print the first and last fruit.

# fruits = ["apple", "banana", "mango"]

# print(fruits[0])
# print(fruits[-1])

# Create a list of marks. Change the second mark to 95 and display the updated list.

# marks = [50, 10, 20.0]
# marks[2] = 95

# print(marks)

# Add 40 using append().
# Add 50 and 60 using extend()

# num = [10 , 30, 30]
# num.append(40)
# num.extend([50 , 60])

# print(num)

# Create a list of student names.

# Insert "Riya" at index 1.

# Remove "Aman"

# name = ["ishaan", "rahul" , "aman"]
# name.insert(1, "riya")
# name.remove("aman")

# print(name)

# Create a list:

# [40, 10, 30, 20]

# Sort it and then reverse it.

# num = [40, 10, 30, 20]
# num.sort()
# num.reverse()

# print(num)

# 1. Create a list containing the names of five programming languages.

# languages = ["python", "java", "c" ,"c++", "sql"]

# print(languages)

# 2. Print the third element and the last element of a list.

# num = [1, 2, 3, 4, 5,]

# print(num[2])
# print(num[-1])

# 3. Create a list of numbers and change the first element to 100.

# num = [1, 5, 50, 100]
# num[0] = 100

# print(num)

# 4. Add "Python" to the end of a list using append().

# language = ["c", "c++", "java"]                 
# language.append("python")

# print(language)

# 5. Add three new cities to a list using extend().

# cities1 = ["alwar", "jaipur"]
# cities2 = ["mumbai", "delhi"]
# cities1.extend(cities2)

# print(cities1)

# 6. Insert "Laptop" at index 2 in a list of electronic items.

# items = ["mobile", "computer", "ps5"]
# items.insert(2 , "laptop")

# print(items)

# 7. Remove "Banana" from a list of fruits.

# fruits = ["apple", "banana", "mango"]
# fruits.remove("banana")

# print(fruits)

# 8. Remove the last element of a list using pop().

# num = [10, 20, 30, 40, 50, 60]
# num.pop[(-1)]

# print(num)

# 9. Sort the list:

# ```
# [90,40,60,20,80]
# ```

# in ascending order.

# num = [90,40,60,20,80]
# num.sort()

# print(num)

# 10. Reverse the following list:

# ["Monday","Tuesday","Wednesday","Thursday"]

# days = ["Monday","Tuesday","Wednesday","Thursday"]
# days.reverse()

# print(days)

# Create a nested list containing three students and their ages. Print each student's name and age.

# students = [
#     ["ishaan", 18],
#     ["karan", 19],
#     ["lakshit", 17]
# ]

# for i in students:
#     print(i[0])
#     print(i[1])

# Create a nested list of three books and their prices. Print the details.

# books= [
#     ["Python",450],
#     ["Java",500],
#     ["C++",400]
# ]

# for book in books:
#     print(book[0],book[1])

# Create a list of squares from 1 to 10 using list comprehension.

# squares = [i * i for i in range(1 , 11)]
# print(squares)

# Create a list of odd numbers from 1 to 20 using list comprehension.

# odd = [i for i in range(1 , 21) if i %2 != 0]
# print(odd)

# Create a list containing only names longer than 5 characters.

# names = ["ishaan", "bob", "alex", "john", "rome"]
# result= [name for name in names if len(name)>5]
# print(result)

# 1. Create a nested list containing five students and their marks.

# students = [
#     ["ishaan", 18],
#     ["bob", 25],
#     ["john", 55],
#     ["alex", 11],
#     ["riya", 99]
# ]

# for i in students:
#     print(i[0])
#     print(i[1])

# 2. Print only the names from a nested student list.

# students = [
#     ["ishaan", 18],
#     ["bob", 25],
#     ["john", 55],
#     ["alex", 11],
#     ["riya", 99]
# ]

# for i in students:
#     print(i[0])

# 3. Update the marks of the second student in a nested list.

# students = [
#     ["ishaan", 75],
#     ["bob", 30],
#     ["john", 45]
# ]

# students[1][1] = 100
# print(students) 

# 4. Create a nested list of three products and calculate the total price.

# 5. Create a list of numbers from 1 to 20 using list comprehension.

# num = [i for i in range(1 , 21)]
# print(num)

# 6. Create a list of cubes from 1 to 10 using list comprehension.

# cube = [i * i * i for i in range(1 , 11)]
# print(cube)

# 7. Create a list of all numbers divisible by 5 between 1 and 100 using list comprehension.

# num = [i for i in range(1 , 101) if i % 5== 0]
# print(num)

# 8. Create a list containing only words that start with the letter "P" from a given list.

# a = ["ishaan", "punit", "putin"]
# char = 'p'
# result = [word for word in a if word.startswith(char)]
# print(result)

# 9. Create a shopping cart with four products and display the total bill.

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

# 10. 10. Create a student marks system that displays the grade:
# A: 90 and above
# B: 75–89
# C: 50–74
# F: Below 50

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