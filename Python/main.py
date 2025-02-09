# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# number1=40
# number2=30

# product=number1*number2
# sum= number1+number2

# if product<=1000:
#     print(f"The multiplication is: {product}")
# else:
#     print(f"The sum is: {sum}")



def calculate_numbers(num1,num2):
    product=num1*num2
    if product <= 1000:
        return product
    else:
        return num1+num2


result= calculate_numbers(20,30)
print(f"The result is: {result}")
result=calculate_numbers(40,30)
print(f"The result is: {result}")


# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

prev_num=0

for i in range(10):
    
    print("current number", i, "prev_num", prev_num ,":", prev_num+i)
    prev_num=i



# Write a Python code to accept a string from the user and display characters present at an even index number.

# user_input= input("Enter string: ")

# print(user_input[::2])


user_input= input("Enter string: ")

print("originsl input", user_input)


size=len(user_input)
for i in range(0,size-1,2):
    print("index[", i, "]", user_input[i])



# Write a Python code to remove characters from a string from 0 to n and return a new string.

# user_input= input("Enter string: ")

# print(user_input[4:])



def remove_chars(word,n):
    x=word[n:]

    print(x)
word=input("Enter word: ")
n=int(input("Enter numbers to remove: "))
remove_chars(word,n)


# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

def check(numlist):
    print("original list", numlist)
    First_num = numlist[0]
    last_num=numlist[-1]

    if First_num == last_num:
        return True
    else:
        return False

print(check([1,2,3,4,1]))


# Write a Python code to display numbers from a list divisible by 5

given_list = [10, 20, 33, 46, 55]
print("Given List:", given_list)
for i in range(len(given_list)):
    if given_list[i] % 5 == 0:
        print(given_list[i])



# Write a Python code to find how often the substring “Emma” appears in the given string.


str_x= input("Enter a string: ")

counting= str_x.count("Emma")
print("Emma appears", counting , "times")


# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5


for i in range(1,6):
    for j in range(1,i+1):
        print(i, end='')
    print()
    


# Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse. For example, 545 is the palindrome number.

