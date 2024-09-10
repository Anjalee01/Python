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



# While loop
# num =1
# while(num <= 5):
#     print(num)
#     num += 1'''

    

height = 80
user_height = float(input("Enter your Height: "))
if(user_height >= height):
  print("You're tall enough to ride!")
else:
  print("You're not tall enough to ride, but maybe next year!")



