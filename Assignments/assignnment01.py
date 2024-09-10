
#Q1 Write a Python program that declares two variables a and b. Assign them any values of your choice.
# Print the result of their sum, difference, multiplication, and division.

a,b = 4.0,6.0
print(a+b)
print(a-b)
print(a*b)
print(a/b)


# Q#2 Write a Python program that demonstrates the use of single-line and multi-line comments.
# Inside the program, print "Hello, Python!" as an example output.

# print("Hello, Python!")


'''print("Hello, Python!")
print("Hello, Python!")
print("Hello, Python!")
print("Hello, Python!")
print("Hello, Python!")'''



# Q#3 Write a Python program that declares a variable name and assigns your name to it.
# Then, print a greeting message such as "Hello, [Your Name]!"

name = "Anjalee"

print (f"Hello, {name}!")


# Q#4 Write a Python program that accepts a number from the user, converts it to a float, and then converts the same number to an integer.
# Print both the float and integer values.

num = int(input("Enter a number"))
print(num)

float_num = float(num)
print(float_num)
integer_num  = int(float_num)
print(integer_num)


# Q5 Write a Python program that declares three variables: an integer, a float, and a string.
# Assign them values and print their data types using the type() function.


a,b,c = 2,  2.0, "Anjalee"
print(type(a))
print(type(b))
print(type(b))



# Q#6 Write a Python program to calculate the area of a rectangle.
# Take the length and width as inputs from the user and print the calculated area.

length = int(input("Enter length: "))
width = int(input("Enter width: "))

area = length*width
print(area)



# Q#7 Write a Python program that initializes a variable x with the value 10.
# Then, use assignment operators (+=, -=, *=, /=, etc.) to modify and print the value of x.

x = 10
print(x)

x+=2
print(x)

x-=4
print(x)

x*=1
print(x)

x/=1
print(x)

x%=2
print(x)

x**=2
print(x)



# Q#8 Write a Python program that takes two numbers as input and compares them using comparison operators (>, <, >=, <=, ==, !=).
# Print the results of the comparisons.

num1= int(input("Enter a num1: "))
num2= int(input("Enter a num2: "))

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)



# Q#9 Write a Python program that takes two integers as input. Use logical operators to check if both numbers are greater than 0.
# Print an appropriate message based on the result.

num1= int(input("Enter a num1: "))
num2= int(input("Enter a num2: "))

if ((num1 > 0) and (num2 > 0)):
  print("Numbers are greater than 0")
else:
    ("Numbers are smaller than 0")




# Q#10 Write a Python program that checks whether the string 'Python' is present in a list of programming languages: ['Java', 'Python', 'C++', 'JavaScript'].
# Use the in operator to check and print the result.

programming_languages = ['Java', 'Python', 'C++', 'JavaScript']

if 'Python' in programming_languages:
  print("Python is present in programming_languages ")
else:
  print("Python is not present in programming_languages ")




# Q#11 Write a Python program that compares two variables x and y using the identity operators (is and is not).
# Assign any values to x and y and print the result of the comparison.

x= 10
y = 4

if x is y:
    print("True")
else:
    print("False")


if x is not y:
    print("True")
else:
    print("False")




# Q#12 Write a Python program that takes two integers as input from the user. Perform addition, subtraction, multiplication, 
# and division on these numbers and print the results.

num1= int(input("Enter a num1: "))
num2= int(input("Enter a num2: "))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)




# Q#13 Write a Python program that takes a string input from the user, 
# converts it into an integer, and multiplies it by 10. Print the result.

user_input = input("Enter a number: ")
integer_value =  int(user_input)
print(integer_value)
print(integer_value * 10)




# Q#14 Write a Python program that initializes two boolean variables a and b with True and False, respectively. 
# Use logical operators (and, or, not) and print the results of the operations.


a,b = True, False

print(a and b)
print(a or b)
print(not a)
print(not b)