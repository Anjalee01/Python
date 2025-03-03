# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

for i in range(len(l1)):
    if i%2 != 0:
        l3.append(l1[i])

for i in range(len(l2)):
    if i%2 == 0:
        l3.append(l2[i])

print(l3)


# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list

sample_list = [34, 54, 67, 89, 11, 43, 94]

element = sample_list.pop(4)

print(element)

sample_list.insert(2, element)
sample_list.append(element)

print(sample_list)



# Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)
    
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    
    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size


# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

count_dict = dict()

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)




# Create a Python set such that it shows the element from both lists in a pair

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)



# Find the intersection (common) of two sets and remove those elements from the first set

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}


common_elements = first_set.intersection(second_set)
print(common_elements)


for item in common_elements:
    first_set.remove(item)


print(first_set)



# Checks if one set is a subset or superset of another set. If found, delete all elements from that set

first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}


print(" First set is subset of second set" , first_set.issubset(second_set))
print(" First set is subset of second set" , second_set.issubset(second_set))

print("First set is superset of second set", first_set.issuperset(second_set))
print("First set is superset of second set", second_set.issuperset(second_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()


print(first_set)
print(second_set)


# Get all values from the dictionary and add them to a list but don’t add duplicates

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

all_values = speed.values()
print(all_values)

speed_list = list()

for val in all_values:
    if val not in speed_list:
        speed_list.append(val)
print(speed_list)



# Remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_list = set(sample_list)
print(unique_list)

tpl = tuple(unique_list)

print(min(tpl), max(tpl))