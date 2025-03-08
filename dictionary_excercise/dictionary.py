# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

myDict = dict()

keys_list = ['Ten', 'Twenty', 'Thirty']
values_list = [10, 20, 30]

for i in range(len(keys_list)):
    myDict.update({keys_list[i] : values_list[i]}) 

print(myDict)


# Merge two Python dictionaries into one


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


dict3= {**dict1,**dict2}
print(dict3)


# Print the value of key ‘history’ from the below

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])


# # Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}


res= dict.fromkeys(employees, defaults)
print(res)


# # Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

new_dict = dict()

for i in sample_dict:
    new_dict.update({i: sample_dict[i]})

print(new_dict)


# # Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}


for i in sample_dict:
    sample_dict.pop(i)

print(sample_dict)



# # Write a Python program to check if value 200 exists in the following dictionary.

sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print("200 present in dict")


# # Write a program to rename a key city to a location in the following dictionary.

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict["location"] = sample_dict.pop('city')
print(sample_dict)

# # Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}


print(min(sample_dict, key=sample_dict.get))


# # Write a Python program to change Brad’s salary to 8500 in the following dictionary.

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500

print(sample_dict)