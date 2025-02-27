# Write a program to create a new string made of an input string’s first, middle, and last character.

str1 = input("Enter string: ")
print(str1)

l = len(str1)
mi = int(len(str1)/2)
res = str1[0] + str1[mi] 
res = res + str1[l-1]
print(res)


# Write a program to create a new string made of the middle three characters of an input string.


str1 = input("Enter string: ")
l = len(str1)
mi = int(l/2)
res  = str1[mi-1: mi+2]
print(res)


# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"

mi = int(len(s1)/2)
print(mi)

s3 = s1[:mi:] + s2 + s1[mi:]
print(s3)




# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

s1 = "America"
s2 = "Japan"

s1mi = int(len(s1)/2)
s2mi = int(len(s2)/2)
first = s1[0]+s2[0]
middle = s1[s1mi] + s2[s2mi]
last = s1[len(s1)-1] + s2[len(s2)-1]
print(first + middle + last)


# Arrange string characters such that lowercase letters should come first


str1 = "PyNaTive"

lowerCase = []
upperCase = []

for char in str1:
    if char.islower():
        lowerCase.append(char)
    else:
        upperCase.append(char)

sorted_str = ''.join(lowerCase+upperCase)
print(sorted_str)



# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

# Total counts of chars, digits, and symbols 

Chars = 0 
Digits =0
Symbol = 0

for i in str1:
    if i.isalpha():
        Chars+=1
    elif i.isdigit():
        Digits+=1
    else: 
        Symbol+=1

print(Chars)
print(Digits)
print(Symbol)



# Create a mixed String using the following rules

# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "Xyz"

length_s1 = len(s1)
length_s2 = len(s2)


length = length_s1 if length_s1 > length_s2 else length_s2

s2 = s2[::-1]

res = ""

for i in length:
    if i < length_s1:
        res = res + s1[i]
    if i < length_s2:
        res = res + s2[i]

print(res)
    

# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

s1 = "Ynf"
s2 = "PYnative"

if s1 in s2:
    print(True)
else:
    print(False)


# def string_balance_test(s1, s2):
#     flag = True
#     for char in s1:
#         if char in s2:
#             continue
#         else:
#             flag = False
#     return flag

# s1 = "Yn"
# s2 = "PYnative"
# flag = string_balance_test(s1, s2)
# print("s1 and s2 are balanced:", flag)

# s1 = "Ynf"
# s2 = "PYnative"
# flag = string_balance_test(s1, s2)
# print("s1 and s2 are balanced:", flag)


# Write a program to find all occurrences of “USA” in a given string ignoring the case.

str1 = "Welcome to USA. usa awesome, usa isn't it?"
sub_str = "USA"

temp_str = str1.lower()

count = temp_str.count(sub_str.lower())
print(count)


# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

str1 = "PYnative29@#8496"

total = 0
cnt = 0

for char in str1:
    if char.isdigit():
        total += int(char)
        cnt +=1
avg = total/cnt

print(avg)


# Write a program to count occurrences of all characters within a string

str1 = "Apple"

char_dict = dict()

for char in str1:
    count = str1.count(char)

    char_dict[char] = count
print(char_dict)



# Reverse a given string

str1 = "PYnative"

str1 = str1[::-1]
print(str1)



# Write a program to find the last position of a substring “Emma” in a given string.

str1 = "Emma is a data scientist who knows Python. Emma works at google."

str2= str1.rfind("Emma")
print(str2)


# Split a string on hyphens

str1 = "Emma-is-a-data-scientist"

sub_strg = str1.split("-")
print(sub_strg)

for sub in sub_strg:
    print(sub)



# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_strng = []
for strng in str_list:
    if strng:
        res_strng.append(strng)
print(res_strng)



# Remove special symbols / punctuation from a string

import string
str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)



# Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'

res = "".join(item for item in str1 if item.isdigit())
print(res)


# Write a program to find words with both alphabets and numbers from an input string.

str1 = "Emma25 is Data scientist50 and AI Expert"

# str1 = 'I am 25 years and 10 months old'

res = "".join(item for item in str1 if item.isalnum)
print(res)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)


# Replace each special symbol with # in the following string


str1 = '/*Jon is @developer & musician!!'

import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)