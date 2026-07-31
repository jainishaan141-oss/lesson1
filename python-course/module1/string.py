# Create a string with your name and print:

# First character
# Last character

# name = "ishaan jain"

# print(name[0])
# print(name[-1])

# Create a string "Programming" and print:

# First 5 characters
# Last 4 characters

# name = "programming"

# print(name[0 : 6])
# print(name[-4 :])

# Convert the following string to uppercase and lowercase.

# Python Programming

# name = "python programming"

# print(name.upper())
# print(name.lower())

# Replace "Java" with "Python".

# I am learning Java

# sen = "i am learning java"

# print(sen.replace("java" , "python"))

# Split the following date into day, month and year.

# 25/12/2026

# date = "25/12/2026"

# print(date.split("/"))

# 1. Create a string containing your full name and print it.

# name = "ishaan jain"
# print(name)

# 2. Print the first, middle and last characters of the string "Engineering".

# field = "engineering"
# print(field[0])
# print(field[5])
# print(field[10])

# 3. Create the string "Artificial Intelligence" and print only "Intelligence" using slicing.

# branch = "artificial intelligence"

# print(branch[11:])

# 4. Convert the string "python programming" to uppercase.

# language = "python programming"
# print(language.upper())

# 5. Convert the string "WELCOME TO COLLEGE" to lowercase.

# name = "WELCOME TO COLLEGE"
# print(name.lower())

# 6. Replace "Delhi" with "Mumbai" in the string:

# city = " i love delhi"
# print(city.replace("delhi" , "mumbai"))

# 7. Split the string:

# fruits = "Apple ,Mango ,Banana , Grapes"
# print(fruits.split())

# 8. Join the following list using "-":

# date = "10-08-2026"
# print(date.split("-"))

# 9. Remove extra spaces from the string:

# name = "     ishaan     "
# print(name.strip())

# Write a program that:

# - Takes the user's full name as input.
# - Prints it in uppercase.
# - Prints it in lowercase.
# - Prints the first character.
# - Prints the last character.

# name = input("enter name:")

# print(name.upper())
# print(name.lower())
# print(name[0])
# print(name[5])

# Write a program to check whether the word "Python" exists in a sentence.

# sentense = "python is very good language"
# print("python" in sentense)

# Count how many times the letter "a" appears in a word.

# word = "appears"
# print(word.count("a"))

# Display the following using an f-string:

# name = "ishaan"
# collge = "skit"
# print(f"my name is {name} and i took addmission in {collge}")

# Count the number of words in a sentence.

# sentence = "INDIA is democratic country and will rule all over world"
# word = sentence.split()
# print(len(word))

# 1. Check whether "Python" exists in a sentence entered by the user.

# text = "python programming"

# print("python" in text)

# 2. Find the index of "College" in a string using find().

# text = "skit college"

# print(text.find("college"))

# 3. Count how many times the letter "e" appears in a sentence.

# text = "sentence"

# print(text.count("e"))

# 4. Check whether a string starts with "Hello".

# text = "hello sir welcome back"

# print(text.startswith("hello"))

# 5. Check whether a filename ends with ".txt".

# file = "ishaan.txt"

# print(file.endswith(".txt"))

# 6. Display student details using an f-string.

# name = "ishaan"
# age = 18

# print(f"my name is {name} , i am {age} years old")

# 7. Create a simple email formatter using format().

# email = "ishaanjain@gmail.com"

# print("email:", email)

# 8. Write a password checker that verifies only the minimum length of 8 characters.

# password = input("enter password:")

# if len(password) == 8:
#     print("password correct")
# else :
#     print("password wrong") 

# 9. Count the number of words and characters in a sentence.

# text = "i am ishaan jain from alwar"

# print(text.count("char"))

# 10. Write a palindrome checker that ignores uppercase and lowercase letters.

# user = input("enter palindrome:").lower()

# if user == user[::-1]:
#     print("correct palindrome")
# else:
#     print("wrong palindrome")