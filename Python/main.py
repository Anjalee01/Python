# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# number1=40
# number2=30

# product=number1*number2
# sum= number1+number2

# if product<=1000:
#     print(f"The multiplication is: {product}")
# else:
#     print(f"The sum is: {sum}")



# def calculate_numbers(num1,num2):
#     product=num1*num2
#     if product <= 1000:
#         return product
#     else:
#         return num1+num2


# result= calculate_numbers(20,30)
# print(f"The result is: {result}")
# result=calculate_numbers(40,30)
# print(f"The result is: {result}")


# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# prev_num=0

# for i in range(10):
    
#     print("current number", i, "prev_num", prev_num ,":", prev_num+i)
#     prev_num=i



# Write a Python code to accept a string from the user and display characters present at an even index number.

# user_input= input("Enter string: ")

# print(user_input[::2])


# user_input= input("Enter string: ")

# print("originsl input", user_input)


# size=len(user_input)
# for i in range(0,size-1,2):
#     print("index[", i, "]", user_input[i])



# Write a Python code to remove characters from a string from 0 to n and return a new string.

# user_input= input("Enter string: ")

# print(user_input[4:])



# def remove_chars(word,n):
#     x=word[n:]

#     print(x)
# word=input("Enter word: ")
# n=int(input("Enter numbers to remove: "))
# remove_chars(word,n)


# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

# def check(numlist):
#     print("original list", numlist)
#     First_num = numlist[0]
#     last_num=numlist[-1]

#     if First_num == last_num:
#         return True
#     else:
#         return False

# print(check([1,2,3,4,1]))


# Write a Python code to display numbers from a list divisible by 5

# given_list = [10, 20, 33, 46, 55]
# print("Given List:", given_list)
# for i in range(len(given_list)):
#     if given_list[i] % 5 == 0:
#         print(given_list[i])



# Write a Python code to find how often the substring “Emma” appears in the given string.


# str_x= input("Enter a string: ")

# counting= str_x.count("Emma")
# print("Emma appears", counting , "times")


# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end='')
#     print()
    


# Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.

# def check_palindrom(number):
#     print("Original Number:", number)
#     original_num = number

#     reverse_num = 0

#     while number > 0:
#         reminder = number % 10
#         reverse_num = (number*10)+reminder
#         number = number//10


#         if original_num == reverse_num:
#             print("Given number is palindrom")
#         else:
#             print("Given number is not palindrom")

# print(check_palindrom(125))
# print(check_palindrom(121))



# def palindrome(number):
#     print("original number", number)
#     original_num = number
    
#     # reverse the given number
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10

#     # check numbers
#     if original_num == reverse_num:
#         print("Given number palindrome")
#     else:
#         print("Given number is not palindrome")

# palindrome(121)
# palindrome(125)


# Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# List3= []

# for i in range(len(list1)):
#     if list1[i] %2!=0:
#         List3.append(list1[i])

# for j in range(len(list2)):
#     if list2[j] %2==0:
#         List3.append(list2[j])
# print(List3)


# Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# number=1234
# print("Given Number", number)

# while number>0:

#     digit = number%10

#     number = number//10

#     print(digit, end="")





# income = 45000
# tax_payable = 0
# print("Given income", income)

# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # no tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_payable = x * 10 / 100
# else:
#     # first 10,000
#     tax_payable = 0

#     # next 10,000 10% tax
#     tax_payable = 10000 * 10 / 100

#     # remaining 20%tax
#     tax_payable += (income - 20000) * 20 / 100

# print("Total tax to pay is", tax_payable)



# Print multiplication table from 1 to 10

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j ,end=" ")
#     print("\t\t")
   


# x="1234444"
# print(id(x))

# y=123
# print(id(y))


# Print a downward half-pyramid pattern of stars

# * * * * *  
# * * * *  
# * * *  
# * *  
# *

# def decresing_pattern(n):
#     for i in range(1,n):
#         for j in range(i,n):
#             print("*", end="")
#         print()
    

# decresing_pattern(5)

    

# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# Note here exp is a non-negative integer, and the base is an integer.
 
# def exponent(base, exp):
#     if exp>=0:
#         value = base**exp
#         print(value)

# exponent(5,4)


# def exponent(base, exp):
#     num = exp
#     result = 1
#     while num > 0:
#         result = result * base
#         num = num - 1
#     print(base, "raises to the power of", exp, "is: ", result)

# exponent(5, 4)


