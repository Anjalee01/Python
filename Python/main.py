# a=10
# b=2

# print(a,b)

# # #Escape  sequence words 
# # #use of \n (for break line )
# # print("This is the list of products: \n mobiles \n laptops")

# # #use of \t (for tab)
# # print("word1\tword2") 


# #use of \ (for unique words)
# print ("u03A9")
# print("\u03A9")

# print ("Quid said: \"work, work work\"")


# Typecasting = Converting one datatype to another.

# a = 46.67
# print (a)

# b= int(a)
# print ("converting int datatype", b)

# c= str(a)
# print("string datatype", c)

# # how to chech datatype of variables. 
 
# a = 23.45
# b = 45 
# c = "hello"

# print(type(a))
# print(type(b))
# print(type(c))



# OPERATORS
# ARTHEMATIC OPERATORS 

# Addition Operator(+)
'''a=5
b=6

print("The sum of the two variables is:", a+b)

# Substraction Operator(-)
a=6
b=6

print("The sum of the two variables is:", a-b)


# Modulus Operator(%)
a=6
b=5

print("The sum of the two variables is:", a%b)

# Power Operator(**)
a=3
b=2

print("The sum of the two variables is:", a**b)

# Multipilication Operator(*)
a=3
b=2

print("The sum of the two variables is:", a*b)

# Division Operator(/)
a=5
b=2

print("The sum of the two variables is:", (a/b))

# Floor division Operator(//)
a=5
b=2

print("The sum of the two variables is:", (a//b))'''

# CONDITIONS
# IF Condition

# a=5
# b=10
# if a > b:
#     print ("A  is greater than b")
#     print ("Be enough")
# print ("Hello world")


# a=5
# b=10
# if a > b:
#     print ("A  is greater than b")
# else:
#     print ("B is greater than A")

# age = int(input("Enter your age "))

# if age >= 18:
#     print("Eligible for giving vote")
# else:
#     print ("Not eligible")


''' age = 18
# int(input("Enter your age "))

# if age >= 18:
#     print("You are eligibale to give vote")

# else:
#     print("Not eligible")



# passenger = (input("Enter terminal: "))

# if passenger == "lahore":
#     print("Go to teriminal 1 ")

# elif passenger == "fsd":
#     print("Go to terminal 2 ")

# elif passenger == "isl":
#     print("Go to terminal 3")
# else:
#     print("SORRY ")


 
# LOGICAL OPERATORS
# AND, OR, NOT

# a,b,c= 10,20,30

# if a >b or a>c: print("A is less than all")
# elif b<a or a>c: print("B is greater than A")
# elif b>a and c<b: print ("C is greater than all")

# else: print("Nothing is true")


# NESTED IF  
# if statement inside an if statement 

# marks = int(input("Enter your marks: ")) 

# if marks >=60:
#     if marks >= 80:
#         print("Pass with excellent performance")
#     else: print("Pass. but need some improvement")
# else: print("Fail")

# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")

# if age >= 18:
#     if gender == "male":
#         print("Go to destination 1")
#     elif gender == "female":
#         print("Go to destination 2")
#     else: print("Go to destination 3 ")
# else: print("Not eligibe for vote")


# Bult in functions in python

# 1. Length
# str = "abcabcabcabc"
# length = len(str)
# print (length)

# 2.Index
# str = "Hello World"
# print(str[3])

# stv = "Hello       world"
# length = len(stv)
# print(length)
# print(stv[3])

# 3.Slicing
# String me se sub string nikalne ke liye use hota hai.

# Identity Operator
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.


# a= [1,2,3]
# b= a
# c= [1,2,3]
# print(id(a))
# print(id(b))
# print(id(c))

# print (a is b)

# print(a is c)

# == checks if the values are same then it will give  true
# print(a == c)

'''

# While loop
# num =1
# while(num <= 5):
#     print(num)
#     num += 1

    

# height = 80
# user_height = float(input("Enter your Height: "))
# if(user_height >= height):
#   print("You're tall enough to ride!")
# else:
#   print("You're not tall enough to ride, but maybe next year!")



# i = 1
# while i<=5:
#     print(i)
#     i+=1


# i = ["Ali", 3, 8]

# print(i)
# for a in i:
#   print(a)




# import random

# guess_chances = 0
# num = random.randint(1, 10)



# while True:


 
 
#  guess = int (input("Enter a guess num:"))
#  if(guess < num ):
#    print("Too Low! Try again") 
#  elif( guess> num):
#   print("Too high!Try try again")
  
#  else:
#   print("Congratulation! You guessed a Num")
#   break
# print("Game is Over")
 

# Problem Statement 1:
# Write a Python program that simulates rolling a six-sided die 10 times. The program should:
# Use a for loop to simulate 10 die rolls.
# Generate a random number between 1 and 6 for each roll.
# Print the result of each roll.


# import random
# for i in range(1,10):
#  roll = random.randint(1, 6)
#  print("Result of roll", roll)










# Problem Statement 2
# Write a Python program that simulates flipping a coin 10 times. The program should:
# Use a for loop to simulate 10 coin flips.
# Generate a random outcome for each flip (either "Heads" or "Tails").
# Count the number of "Heads" and "Tails" outcomes.
# Print the result of each flip.
# Print the total counts of "Heads" and "Tails" at the end.


# import random

# head = 0
# tail = 0

# for i in range(1,10):
# #  coin =["Heads",  "tails"]
#  random_choice = random.choice(["heads", "tails"])
#  print(random_choice)
#  if random_choice == "heads":
#   head +=1
#  else:
#   tail +=1
# print("Count of head is " , head)
# print("Count of tail is " , tail)

  
 
 

# Ask the user for three numbers and calculate their average. Print whether the result is an integer or a floating-point number.

# num1 = int(input("Enter nunm1: "))
# num2 = int(input("Enter nunm2: "))
# num3 = int(input("Enter nunm3: "))

# total_length = len(num1,num2,num3)
# print("total_length")
# avg = ((num1 + num2 + num3)/3)
# print(avg)

# if avg%2==0:
#     print("Number is even")
# else:
#     print("Number is odd")



# Write a program that asks the user for the cost of an item and the amount of money they paid. Print how much change they should receive.
 
# cost = int(input("Enter Cost Of the Item: "))
# amount_paid = int(input("Enter amout you paid: "))
# change = (amount_paid - cost)
# print(f'you should receieve {change} back')


# Write a program that calculates the greatest common divisor (GCD) of two numbers using a loop.
# Write a program that asks the user to input a month number (1-12) and prints the number of days in that month. Assume February has 28 days.


# Loops:
# Write a program that prints the first 10 natural numbers using a while loop.
 
# i = 1
# while i <11:
#     print(i)
#     i+=1
  
# Ask the user to input a number. Write a program to print all the numbers from 1 up to that number using a for loop.

# give_num = int(input("Enter a number: "))


# for i in range(1, give_num + 1 ):
#     print(i)





# Write a program that asks the user for a number and prints the multiplication table for that number up to 10.


# num = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f'{num} x {i} = {num*i}')


# num = 2
# for i in range(1,11):
#     print(f'2 x {i} = {2*i}')




# Write a program that asks the user to input a number and prints whether that number is prime (a prime number is only divisible by 1 and itself).

# num = int(input("Enter a number: "))

# if num%1==0 and num%num==0:
#     print("Prime number")
# else: 
#     print("Not prime number")

# Write a program that calculates the sum of all even numbers between 1 and 100 using a loop.

# for i in range(1,111):
#     if i%2==0:


# Write a program to print the factorial of a number entered by the user using a loop. (Factorial of n is n * (n-1) * ... * 1)

# DATA STRUCTURE

# Here are some medium-level practical questions that require more problem-solving and logical thinking but still build on the basics:

# Variables and Data Types:
# Write a program to swap the values of two variables without using a third variable. For example, if a = 5 and b = 3, after swapping, a should be 3 and b should be 5.

# Ask the user for three numbers and calculate the average. Then, print whether the average is an integer or a floating-point number.

# Arithmetic and Comparison Operators:
# Write a program to calculate the area of a triangle given its three sides using Heron's formula:

# �
# =
# �
# +
# �
# +
# �
# 2
# s= 
# 2
# a+b+c
# ​
 
# Area
# =
# �
# (
# �
# −
# �
# )
# (
# �
# −
# �
# )
# (
# �
# −
# �
# )
# Area= 
# s(s−a)(s−b)(s−c)
# ​
 
# Create a calculator program that can handle basic arithmetic operations (+, -, *, /, %, **) based on user input for two numbers and the operation.

# Ask the user to input three numbers and print them in ascending order without using any built-in sort function.

# Flow Control (if-else, elif):
# Write a program to determine if a given year is a leap year. (Hint: A year is a leap year if it is divisible by 4 but not by 100, except when it's also divisible by 400.)

# Create a grading system that asks the user for their exam score (0-100) and prints a letter grade:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# Loops:
# Write a program to check if a number is a prime number. A prime number is a number that is divisible only by 1 and itself.

# Create a program that calculates the factorial of a number using a loop (e.g., factorial of 5 is 5 x 4 x 3 x 2 x 1 = 120).

# Write a program that asks the user to input 5 numbers and then calculates the sum of all odd numbers and the sum of all even numbers separately.

# Create a program that prints the Fibonacci series up to n numbers, where n is provided by the user.

# Strings:
# Write a program to check if a string is a palindrome (i.e., it reads the same forwards and backward). Ignore case sensitivity and spaces. For example, "A man a plan a canal Panama" is a palindrome.

# Ask the user to input a string and print the frequency of each character in the string (excluding spaces).

# Create a program to find the longest word in a given sentence input by the user.

# Write a program to capitalize the first letter of each word in a given sentence.

# Lists:
# Write a program to rotate the elements of a list by a given number k. For example, if the list is [1, 2, 3, 4, 5] and k = 2, the output should be [4, 5, 1, 2, 3].

# Given a list of integers, create a program to find the second largest number in the list.

# Write a program to take a list of numbers as input and then create a new list that contains only the even numbers from the original list.

# Write a program that asks the user to input 10 numbers into a list. Then, print how many times the largest number appears in the list.

# Tuples:
# Create a program that takes a tuple of integers and prints the elements in reverse order.

# Write a program to merge two tuples into a single tuple without using the + operator (try using loops).

# Given a tuple of numbers, write a program to find the sum and the product of all elements in the tuple.

# Sets:
# Create two sets of integers from user input and find their union, intersection, and difference.

# Write a program that takes a list of words from the user and stores them in a set. Then, check if a specific word is in the set and print "Yes" or "No."

# Given two sets, write a program to check if one set is a subset of another.

# Combined Challenges:
# Write a program that generates a list of 20 random numbers between 1 and 100, then counts how many of them are divisible by both 3 and 5.

# Create a number guessing game where the program picks a random number between 1 and 50. The user has 5 attempts to guess the number. After each guess, the program should tell the user whether their guess was too high, too low, or correct.

# Write a program to simulate the roll of two dice. After rolling the dice, calculate and print the sum. If the sum is 7 or 11, print "You win!"; otherwise, print "You lose."

# Write a program to sort a list of words in alphabetical order without using any built-in sorting function.

# Create a program that simulates a basic ATM system:

# Ask the user for their initial balance.
# Provide options to Deposit, Withdraw, or Check Balance.
# Update the balance based on the user's actions and allow them to perform multiple transactions.
# Strings and List Combination:
# Write a program that takes a sentence from the user and reverses the order of the words in the sentence, while keeping the words themselves unchanged.

# Given a list of words, write a program to find all the words that are longer than a user-specified length.

# Advanced String Manipulation:
# Write a program to find all the unique characters in a given string and print them in the order of their first appearance.

# Write a program to count the occurrences of each vowel in a string (ignore case sensitivity) and print the result.

# These questions require students to use loops, conditionals, data structures, and some level of logic and creativity. They help transition students from basic programming exercises to problems that require multiple concepts to be used together.






# You said:
# Give questions that are bit easier than this
# ChatGPT said:
# ChatGPT
# Here are some medium-easy level practical questions that are a step up from the beginner ones but easier than the previous set:

# Variables and Data Types:
# Write a program that takes two numbers as input from the user and swaps their values using a third variable. Print the values before and after swapping.

# Write a program that asks for the user's name, and then prints a message "Your name has X characters", where X is the length of the user's name.

# Arithmetic and Comparison Operators:
# Write a program that asks the user to input the radius of a circle and then calculates and prints the area and circumference of the circle.

# Area = 
# �
# �
# 2
# πr 
# 2
 
# Circumference = 
# 2
# �
# �
# 2πr
# Assume 
# �
# =
# 3.14
# π=3.14.
# Write a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

# Flow Control (if-else, elif):
# Write a program that asks the user to input their age.

# If they are less than 12, print "You are a child".
# If they are between 13 and 19, print "You are a teenager".
# Otherwise, print "You are an adult".
# Write a program that asks the user to input a number and checks whether it is even or odd.

# Loops:
# Write a program that prints the numbers from 1 to 20 using a for loop.

# Write a program that asks the user for a number and prints the multiplication table of that number up to 10.

# Write a program that calculates the sum of all numbers from 1 to 50 using a for loop.

# Write a program that asks the user for a word and prints each letter of the word on a new line using a for loop.

# Strings:
# Write a program to take a sentence as input and print the number of words in that sentence.

# Ask the user for their name and then print the name in reverse order.

# Write a program that asks the user to input a string and counts how many vowels (a, e, i, o, u) are in the string.

# Write a program that takes a string as input and replaces all the spaces with hyphens (-).

# Lists:
# Write a program to create a list of five numbers entered by the user and then find the largest number in the list.

# Create a list of numbers from 1 to 10. Write a program to print the sum of all the numbers in the list.

# Write a program to ask the user for five numbers and store them in a list. Then, reverse the list and print it.

# Create a list of 10 numbers. Write a program to print only the odd numbers from that list.

# Write a program to take 5 numbers as input and store them in a list. Then, sort the list in descending order and print it.

# Tuples:
# Write a program to create a tuple of five numbers and print the smallest and largest numbers in the tuple.

# Create a tuple with three different fruit names and print them one by one using a for loop.

# Sets:
# Create a program that takes 5 unique numbers as input from the user and stores them in a set. Then, print the set.

# Write a program to create two sets of numbers and print their union and intersection.

# Ask the user for 5 numbers, store them in a set, and then check if the number 7 is in the set or not.

# Combined Challenges:
# Write a program that takes a sentence as input from the user and converts it into a list of words. Then, print the list.

# Create a list of 5 student names and a separate list of their marks. Write a program that prints each student's name along with their corresponding mark.

# Write a program to take a number from the user and check if it is a prime number (a number that is only divisible by 1 and itself).

# Write a program that takes a list of 5 numbers and creates a new list containing the squares of each number.

# Create a program that simulates a rock-paper-scissors game between the user and the computer. The user inputs their choice, and the program randomly chooses rock, paper, or scissors.

# Write a program that generates a random number between 1 and 10 and asks the user to guess the number. Print a message whether their guess was correct or not.

# String and List Combination:
# Write a program that takes a string as input and splits it into a list of words. Then, print the words in reverse order.

# Ask the user to input a sentence. Then, print the sentence with every second word in uppercase.

# Logic and Decision Making:
# Write a program to find the second largest number in a list of 10 numbers provided by the user.

# Write a program to check if two words provided by the user are anagrams of each other (i.e., they contain the same letters in a different order).



# Create a dictionary:
# Define a dictionary that stores the names of three fruits and their corresponding colors.


# fruits={
#     "apple": "red",
#     "mango": "yellow",
#     "grapes": "Green"
# }
# print((fruits))

# Access a value using a key:
# Given the dictionary fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}, how can you access the color of a banana?

# fruit_colors = {
#     'apple': 'red',
#     'banana': 'yellow', 
#     'grape': 'purple'
# }

# print(fruit_colors['banana'])

# Add a new key-value pair:
# Add a new fruit, 'orange', with the color 'orange' to the dictionary fruit_colors = {'apple': 'red', 'banana': 'yellow'}.

# fruit_colors = {
#     'apple': 'red',
#     'banana': 'yellow', 
#     'grape': 'purple'
# }

# fruit_colors['orange']='orange'

# fruit_colors.update({'orange':'orange'})
# print(fruit_colors)

# Update a value
# If fruit_colors = {'apple': 'red', 'banana': 'yellow'}, update the color of the apple to 'green'.

# Remove a key-value pair:
# In the dictionary fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}, remove the 'grape' entry.

# fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}

# fruit_colors.popitem()
# print(fruit_colors)
# fruit_colors.pop('apple')
# print(fruit_colors)


# Check if a key exists:
# Given fruit_colors = {'apple': 'red', 'banana': 'yellow'}, check if the key 'banana' exists in the dictionary.

# fruit_colors = {'apple': 'red', 'banana': 'yellow'}

# print('apple' in fruit_colors)

# if 'apple' in fruit_colors:
#     print("Apple is present in dict")
# else:
#     print("Apple is not in the list")


# Iterate over keys:
# Given the dictionary fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}, write a loop to print all the keys.

# fruit_colors = {
#     'apple': 'red', 
#     'banana': 'yellow', 
#     'grape': 'purple'
# }

# for i in fruit_colors:
#     print(i)
# Iterate over values:
# Given the same dictionary, write a loop to print all the values.


# fruit_colors = {
#     'apple': 'red', 
#     'banana': 'yellow', 
#     'grape': 'purple'
# }

# for i  in fruit_colors:
#     print(i, fruit_colors[i])


# Create an empty dictionary:
# How do you create an empty dictionary and add a key 'name' with the value 'John' to it?

# dict = {}

# dict['name'] ='John'

# print(dict)



# my_dict = {'x': 10, 'y': 20, 'z': 30}
# print(my_dict['y'])








#Swap keys and values:
#Given the dictionary fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}, 
#create a new dictionary that swaps the keys and values so that the colors become keys and the fruits become values.

# fruit_colors = {
#     'apple': 'red', 
#     'banana': 'yellow', 
#     'grape': 'purple'
# }






# Merge two dictionaries:
# Given two dictionaries:


# Combine them into a new dictionary, ensuring that if there are duplicate keys, the values from dict2 overwrite those in dict1.

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# dict3 = (dict1 + dict1)
 
# for i in dict1 and dict2:
#     if i == i:


# print(dict3)

# Count occurrences of values:
# Given the dictionary votes = {'Alice': 'Python', 'Bob': 'Java', 'Charlie': 'Python', 'David': 'C++'}, count how many people voted for 'Python'.


# votes = {
#     'Alice': 'Python', 'Bob': 'Java', 'Charlie': 'Python', 'David': 'C++'
#     }


# for i in votes:
#     if votes[i] == 'Python':
#         print(i)


# Find key with the maximum value:
# Given the dictionary scores = {'Alice': 50, 'Bob': 75, 'Charlie': 100, 'David': 65}, find the key (person's name) with the highest score.

# scores = {'Alice': 50, 'Bob': 75, 'Charlie': 100, 'David': 65}


# for i in scores:
#     if scores[i] == max:
#         print(i)

# Create a dictionary from two lists:
# You have two lists:

# python
# Copy code
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# Create a dictionary where the names are the keys and the ages are the values.

# Find common keys between two dictionaries:
# Given the dictionaries:

# python
# Copy code
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}
# Find the keys that are present in both dictionaries.

# Remove key if condition is met:
# Given the dictionary numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4}, remove any key-value pair where the value is even.

# Sum values of a dictionary:
# Given the dictionary expenses = {'rent': 1200, 'groceries': 300, 'utilities': 150}, calculate the total sum of all the values.

# Nested dictionary access:
# Given the dictionary:


# How would you access the value 'New York'?
# person = {
#     'name': 'Alice',
#     'age': 25,
#     'address': {'city': 'New York', 'zipcode': 10001}
# }


# print(person['address']['city'])

# Dictionary comprehension:
# Given the list numbers = [1, 2, 3, 4, 5], create a dictionary where each number is a key, and its value is the square of the number (e.g., {1: 1, 2: 4, 3: 9}).

# These questions are still accessible but require a bit more thought about how to manipulate dictionaries.