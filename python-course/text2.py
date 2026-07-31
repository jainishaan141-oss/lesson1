# Q1. Which loop is generally used when the number of iterations is known?

# A. while loop

# B. for loop

# C. if statement

# D. break

# b(for loop)

# Q2. What is the output?
# for i in range(3):
#     print(i)

# A.

# 1 2 3

# B.

# 0 1 2

# C.

# 0 1 2 3

# D.

# 1 2

# b(0 1 2)

# Q3. Which function is commonly used with a for loop to generate numbers?

# A. input()

# B. print()

# C. range()

# D. len()

# c(range())

# Q4. What is the output?
# i = 1

# while i <= 3:
#     print(i)
#     i += 1

# A.

# 1
# 2
# 3

# B.

# 0
# 1
# 2

# C.

# 1
# 2

# D. Infinite Loop

# a(1 2 3)

# Q5. Which statement is true about a while loop?

# A. It always executes once.

# B. It repeats while the condition is True.

# C. It cannot use conditions.

# D. It always uses range().

# b(it repeats while the condition is true)

# Q6. A nested loop means:

# A. A loop after another loop

# B. A loop inside another loop

# C. Two if statements

# D. A function inside a loop

# b(a loop inside another loop)

# Q7. How many times will the inner loop execute?
# for i in range(2):
#     for j in range(3):
#         print("*")

# A. 2

# B. 3

# C. 5

# D. 6

# b(3)

# Q8. What is the first value produced by range(5)?

# A. 1

# B. 5

# C. 0

# D. 2

# c(0)

# Q9. Which loop is most suitable when the number of repetitions is unknown?

# A. for loop

# B. while loop

# C. nested loop

# D. if statement

# b(while loop)

# Q10. Which keyword is used to start a while loop?

# A. for

# B. loop

# C. while

# D. repeat

# c(while)

# Section B – Find and Fix the Errors (5 × 2 = 10 Marks)

# Correct the errors in the following programs.

# Q1.
# for i range(5):
#     print(i)

# for i in range(5):
#     print(i)

# Q2.
# i = 1
# while i <= 5
#     print(i)
#     i += 1

# i = 1
# while i <=5:
#     print(i)
#     i += 1

# Q3.
# for i in range(3):
# print(i)

# for i in range(3):
#     print(i)

# Q4.
# for i in range(2):
#     for j in range(3)
#         print("*")

# for i in range(2):
#     for j in range(3):
#         print("*")

# Q5.
# i = 1
# while i <= 5:
#     print(i)

# while i <=5:
#     print(i)

# # Section C – Theory Questions (5 × 2 = 10 Marks)

# Answer the following questions.

# Q1.

# What is a loop? Why do we use loops in programming?

# we use loops in python because we don't write one sentences many times but take the help of loop we print many statement in onr e time

# Q2.

# Write two differences between a for loop and a while loop.

# for loop -- we know the range of numbers , how many times statement executes
# while loop -- we don't know about range, and also don't know about how many times statement executes

# Q3.

# What is a nested loop? Give one real-life example.

# nested loop -- when one loop inside another loop
# ex. -- holla

# Q4.

# What does range(1, 6) generate?

# first we make a for loop and write range of numbers. numbers range is 1 to 6 and  give the command of print after the output is 1 2 3 4 5 because in loops ending number never executes

# Q5.

# What will happen if the loop variable is not updated inside a while loop?

# when we don't update lop variable inside while loop then while loop is not run properly and give some error

# Section D – Coding Questions (5 × 2 = 10 Marks)

# Write Python programs for the following.

# Q1.

# Print numbers from 1 to 10 using a for loop.

# for i in range(1 , 11):
#     print(i)

# Q2.

# Print all even numbers from 2 to 20 using a while loop.

# for i in range(2 , 20 , 2):
#     print(i)

# Q3.

# Print the following pattern using nested loops:

# *
# * *
# * * *
# * * * *

# for i in range(1 , 5):
#     for j in range(i ):
#          print("*" , end = " ")
#     print()

# Q4.

# Print the multiplication table of 7.

# Example:

# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

# num = int(input("enter number:"))

# for i in range(1 , 11):
#     print(num , "x" , i , "=" , num * i)

# Q5.

# Print the following pattern:

# 1 2 3
# 1 2 3
# 1 2 3

# for i in range(1 , 4):
#     for j in range(1 ,4):
#         print(j , end = " ")
#     print() 

# using nested loops.