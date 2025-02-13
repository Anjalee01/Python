# Write a program to accept two numbers from the user and calculate multiplication

num1 = int(input("Input a number: "))
num2 = int(input("Input a number: "))

multiple = num1*num2
print(multiple)


# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”

print("Name","is","james")
print('My', 'Name', 'Is', 'James' , sep="**")


# Display float number with 2 decimal places using

num =458.541315
print("%.3f" % num)


# Convert Decimal number to octal using print() output formatting

num =8
print('%o' % num)




#  Accept a list of 5 float numbers as an input from the user

number = []

for i in range(0,5):
    print("Enter number at a location",i,":")

    item = float(input())
    number.append(item)
print(number)


# Write all content of a given file into a new file by skipping line number 5



with open("text.txt","w") as fp:
    for i in range(1,8):
        fp.write(f"line{i} \n")

with open(r"D:\I\Python\input_output_exercise\text.txt", "r") as fp:
    lines = fp.readlines()

# with open(r"D:\I\Python\input_output_exercise\new_file.txt", "w") as fp:
    count = 0
    for line in lines:

        if count == 4:
            count+=1
            continue
        else:
            fp.write(line)
        count+=1


# Write a program to take three names as input from a user in the single input() function call.

str1, str2, str3 = input("Enter three string: ").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)


# Write a program to use string.format() method to format the following three variables as per the expected output

totalMoney = 1000
quantity = 3
price = 450

# statement = "I have {1} dollars so I can buy {0} football for {2:.2f%} dollars."
# print(statement.format(quantity,totalMoney,price))