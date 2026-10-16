#-----------------------------------------------------------------------------
# Name:        Lists (lists.py)
# Purpose:     Demonstrating creating lists, indexes, slices, looping through
#              lists, 'in', and list methods
#
# Author:      Mr. Kowalczewski
# Created:     28-Sept-2026
# Updated:     28-Sept-2026
#-----------------------------------------------------------------------------

# --- Creating lists ----------------------------------------------------------
fruit = ['apple', 'pear', 'peach', 'banana', 'pineapple']
numbers = [5, 3, 2, 4, 1, 6, 8, 10]
bools = [True, False, True, True]

print(fruit)
print(numbers)


# --- Accessing items ---------------------------------------------------------
# accessing individual values
print(fruit[4])
print(fruit[0])

# IndexError occurs if you try to access an index value that doesn't exist
#print(fruit[10])

# negative index (backwards)
print(fruit[-1])
print(fruit[-3])

# slices (not including the last index value)
print(fruit[1:4])
print(fruit[-1:-3:-1])

# you can use these values like any other variable
if fruit[0] == 'apple':
    print('Found an apple')

# does this make sense? Can a list be equal to a string?
if fruit == 'apple':
    print('Found an apple')

# using len(), it is easy to loop through a list
# i represents each index value from 0 to the end
print('Starting Loop:')
for i in range(0, len(fruit), 1):
    if fruit[i] == 'pear':
        print("PEAR")
    print(fruit[i])


# --- in ----------------------------------------------------------------------
fruit = ['apple', 'pear', 'peach', 'banana', 'pineapple']

# directly checking if 'peach' is in the fruit list
if 'peach' in fruit:
    print('FOUND A PEACH')

# each value in the list is stored into 'item' one at a time
for item in fruit:
    item += "'s are great!"
    print(item)

# looping through the index values allows direct changes to the list
for i in range(0, len(fruit), 1):
    fruit[i] += "'s are great!"
    print(fruit[i])

print(fruit)


# --- List methods ------------------------------------------------------------
fruit = ['apple', 'pear', 'peach', 'banana', 'pineapple', 'peach']
# empty list
numbers = []

# add to the end of the list
fruit.append('grape')
print(fruit)
numbers.append(5)
numbers.append(2)
print(numbers)

# add at a specific location
fruit.insert(5, 'kiwi')
print(fruit)

# sort the list
fruit.sort()
print(fruit)
numbers.sort()
print(numbers)

# remove the first instance of a value
fruit.remove('peach')
print(fruit)

# remove (and return) the last item
last_fruit = fruit.pop()
print(last_fruit)
print(fruit)
