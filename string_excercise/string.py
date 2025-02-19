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