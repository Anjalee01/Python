# Print first 10 natural numbers using while loop

n=1

while n<=10:
    print(n)
    n+=1

# Write a Python code to print the following number pattern using a loop.

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()


# Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

s=0
n = int(input("Give a number: "))
for i in range(1,n+1):
    s+=i
print(s)


# Print multiplication table of a given number

num=2

for i in range(1,11):
    print(num*i)



# Write a Python program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop


numbers = [12, 75, 150, 180, 145, 525, 50]


for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)



# Write a Python program to count the total number of digits in a number using a while loop.

n=75869

count=0
while n!=0:
    n=n//10
    count+=1
print(count)


# Write a Python program to print the reverse number pattern using a for loop.

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()



# Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

new_list = reversed(list1)

for item in new_list:
    print(item)



# Display numbers from -10 to -1 using for loop

for i in range(-10,0):
    print(i)


# Display a message “Done” after the successful execution of the for loop

for i in range(5):
    print(i)
print("Done!")