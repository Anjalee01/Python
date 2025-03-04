# Reverse a list in Python

list1 = [100, 200, 300, 400, 500]

list1.reverse()
print(list1)

print(list1[::-1])



# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

res = [x + y for x,y  in zip(list1, list2)]
print(res)


# Given a list of numbers. write a program to turn every item of a list into its square.

res = []

numbers = [1, 2, 3, 4, 5, 6, 7]

for i in numbers:
    res.append(i*i)
print(res)



# Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)


# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x,y in zip(list1, list2[::-1]):
    print(x,y)



# Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i in list1:
    if i == "":
        list1.remove(i)
print(list1)


res = list(filter(None, list1))
print(res)


# Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)

# you have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]

list1[2][1][2].append(sub_list)
print(list1)


# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break
print(list1) 

list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)

print(index)

list1[index] = 200
print(list1)


# Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]

for i in list1:
    if i == 20:
        list1.remove(20)
print(list1)