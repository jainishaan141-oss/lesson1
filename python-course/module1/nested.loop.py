# Print a rectangle of 3 rows and 6 columns using stars.

# for i in range(3):
#     for j in range(6):
#         print("*", end = " " )
#     print()    


# Print the following pattern:

# 1
# 1 2
# 1 2 3
# 1 2 3 4

# for i in range(1 , 5):
#     for j in range(1, i+1):
#         print(j, end = " ")
#     print()

# Print the following pattern:

# A
# A A
# A A A
# A A A A

# for i in range(1,5):
#     for j in range(i):
#         print("A", end = " ")
#     print()

# Print multiplication tables from 1 to 3.

# for i in range(1,4):
#     print("******", i, "******")

#     for j in range(1,11):
#         print(j, "x", i, "=", j* i )


# 1. Print a rectangle pattern of 5 rows and 5 columns using stars.

# for i in range(5):
#     for j in range(5):
#         print("*" , end = " ")
#     print()

# 2. Print the pattern:

# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1 , 6):
#     for j in range(i):
#         print("*" , end = " ")
#     print()

# 3. Print the pattern:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1 , 6):
#     for j in range(1 , i + 1):
#         print(j , end = " ")
#     print()

# 4. Print the pattern:

# A
# A B
# A B C
# A B C D

# 5. Print multiplication tables from 1 to 10.

# for i in range(1 , 11):
#     print("******" , i , "*******")

#     for j in range(1 , 11):
#         print(j , "x" , i , "=" , j * i)

# 6. Print all coordinates of a 5 × 5 grid.

# for i in range(5):
#     for j in range(5):
#         print(j , end = " ")
#     print()

# 7. Print:

# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5
# 5 5 5 5 5

# for i in range(5):
#     for j in range(5):
#         print("5" , end = " ")
#     print()

# 8. Print the pattern:

# 10
# 10 20
# 10 20 30
# 10 20 30 40

# for i in range(10 , 50):
#     for j in range(1 , i + 10):
#         print(j , end = " ")
#     print()

# 9. Print a square pattern using #.

# # # #
# # # #
# # # #
# # # #

# for i in range(4):
#     for j in range(4):
#         print("#" , end = " ")
#     print()

# 10. Print the pattern:

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1 , 6):
#     for j in range(1 , i):
#          print(j , end = " ")
#     print()

# 10 20 30
# 10 20 30
# 10 20 30

# for i in range(4):
#     for j in range(1 , 4):
#         print(j * 10 , end = " ")
#     print()

# 9 8 7
# 9 8 7
# 9 8 7

# for i in range(3):
#     for j in range(9 , 6 , -1):
#         print(j , end = " ")
#     print()

# 1 4 9 16
# 1 4 9 16
# 1 4 9 16
# 1 4 9 16

# for i in range(4):
#     for j in range(1, 5):
#         print(j * j, end = " ")
#     print()

# A A A A
# B B B B
# C C C C
# D D D D

# for i in range(4):
#     for j in range(4):
#         print(chr(65 + i), end = " " )
#     print()
    
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0

# for i in range(4):
#     for j in range(4):
#         if (i + j) % 2 == 0:
#             print(0, end = " ")
#         else:
#             print(1 , end = " ")
#     print()

# 1. Print a 6 × 6 hollow square using .

# size = 6

# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print(".", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 2. 6
#    6 5
#    6 5 4
#    6 5 4 3
#    6 5 4 3 2
#    6 5 4 3 2 1

# for i in range(6 , 0 , -1):
#     for j in range(6 , i - 1 , -1):
#         print(j , end = " ")
#     print()

# 3. Print a 5 × 5 multiplication grid.

# for i in range(1 , 6):
#     for j in range(1 , 6):
#         print(i * j , end = " ")
#     print()

# 4. Print a 4 × 4 addition table.

# for i in range(1 , 5):
#     for j in range(1 , 5):
#         print(i + j , end = " ")
#     print()

# 5. Print a 5 × 5 subtraction table where each value is row - column.

# for i in range(1 , 6):
#     for j in range(1 , 6):
#         print(i - j , end = " ")
#     print()

# 6. Print the coordinates of a 6 × 6 grid.

# for i in range(6):
#     for j in range(6):
#         print(f"({i}, {j})", end=" ")
#     print()

# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E

# for i in range(5):
#     for j in range(65 , 70):
#         print(chr(j), end = " ")
#     print()

# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E

# for i in range(65 , 70):
#     for j in range(5):
#         print(chr(i), end=" ")
#     print()

# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1

# for i in range(5):
#     for j in range(5):
#         if (i + j) % 2 == 0:
#             print(1 , end = " ")
#         else:
#             print(0 , end = " ")
#     print()

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# for i_start in range(1 , 17 , 4):
#     for j in range(4):
#         print(i_start + j , end = " ")
#     print()

