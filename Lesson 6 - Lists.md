# Lesson 6 - Lists

The example code for this lesson is in `lists.py`. Open it alongside these
notes and run it as we go.

A list (called an array in other languages) is a single variable that holds
more than one piece of information, and it can be changed (it is mutable). Until
now, each variable held one piece of information.

A list can hold any data type, but usually all its items are the same type. You
will usually work with list items one at a time, rather than the whole list.

```python
fruit = ['apple', 'pear', 'peach', 'banana', 'pineapple']
numbers = [5, 3, 2, 4, 1, 6, 8, 10]
bools = [True, False, True, True]

print(fruit)      # ['apple', 'pear', 'peach', 'banana', 'pineapple']
print(numbers)    # [5, 3, 2, 4, 1, 6, 8, 10]
```

A list uses square brackets, with items separated by commas. Each item is
reached by its index:

| index | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| element | `'apple'` | `'pear'` | `'peach'` | `'banana'` | `'pineapple'` |

## Accessing items

```python
fruit = ['apple', 'pear', 'peach', 'banana', 'pineapple']

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
```

- `len()` finds the length of a list (like a string).
- `i` is the usual name for a list index. This is one of the few places a
  single-letter variable name is fine.
- `list_name[i]` gets the item at index `i`.

## in

We have used `in` before. With lists it has two more uses:

```python
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
```

`in` checks whether a value is in the list directly; no loop needed.

A `for ... in` loop stores each item in the variable `item`, moving to the next
one each time. Use it when you do not need to change the list: changes to
`item` are not saved back to the list. Looping with `list_name[i]` lets you
change the list directly.

## List methods

Like strings, lists have methods. Unlike strings, list methods change the list
itself.

```python
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
```

There are more list methods that you may find useful:
https://www.w3schools.com/python/python_ref_list.asp

## Lab

That is it for the lesson. Move on to Lab 6, in `README.md`.
