# 1. Create a list of 15 numbers and count how many are divisible by 3.

# number = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# divisible_num = [num for num in number if num % 3 == 0]
# count = len(divisible_num)
# print("num divisible by 3:", divisible_num)
# print("total count:", count)

# 2. Create a list of student marks and print only the marks greater than 80.

# marks = [85, 55, 100, 65, 40]
# greater_mark = [mark for mark in marks if mark > 80]
# print("marks greater than 80:", greater_mark)

# 3. Create a list of numbers and create another list containing only the even numbers.

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_num = [num for num in number if num %2 == 0]
# print("even number:", even_num)

# 4. Create a list of names and print the longest name without using max().

# names = ["ishaan", "bob", "john", "lakshit", "rohan"]
# for name in names :
#     if len(name) > 5:
#         print(name)

# 5. Create a tuple of five temperatures and find the highest and lowest temperature without using max() or min().

# temperarure = [15.5, 10, 5.5, 35, 45.8]
# highest_temp = temperarure[0]
# smallest_temp = temperarure[0]
# for temp in temperarure:
#     if temp > highest_temp :
#           highest_temp = temp
#     if temp < highest_temp:
#          lowest_temp = temp

# print("highest temprature:", highest_temp)
# print("lowest temprature:", smallest_temp)

# 6. Create a tuple of employee salaries and count how many salaries are greater than ₹40,000.

# salaries = [50000, 40000, 100000, 55000, 35000]
# for salary in salaries:
#     if salary > 40000:
#         print(salary) 

# 7. Create a tuple of five subject names and display each subject with its index.

# subject = ["math", "physics", "english", "chemistery", "hindi"]
# print(subject[0])
# print(subject[1])
# print(subject[2])
# print(subject[3])
# print(subject[4])

# 8. Create a nested list containing student names and marks. Display only the students who scored 80 or above.

# student = [
#     ["ishaan", 95]
#     ["bob", 80]
#     ["john", 81]
# ]
# count=0
# for mark in student:
#     if mark > 80:
#         count+=1
#         print(student[0 , 1])
# print("Students Above 80 =",count)

# 9. Create a shopping cart using a list containing product prices. Calculate:
# - Total bill
# - Average price
# - Highest price (without using `max()`)

# cart_price = [2000, 50000, 1000, 100, 40000]
# total_bill = 0
# highest_price = cart_price[0]
# for price in cart_price:
#     total_bill += price
#     if price > highest_price:
#          highest_price = price
#     if len(cart_price) > 0:
#         average_price = total_bill / len(cart_price)
# print(f"Total Bill:{total_bill}")
# print(f"Average Price:{average_price}")
# print(f"Highest Price:{highest_price}")

# 10. Create a tuple containing the coordinates of five points:

# points = ((2,3), (4,5), (6,7), (8,9), (10,11))
