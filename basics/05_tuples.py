# Python Tuples 
'''
Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.
'''

# Create a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Get a value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears' TypeError: 'tuple' object does not support item assignment

numbers = tuple((1,2,3,4,5,6,7,8,9))

# Get Length
print(len(numbers))

# Delete a tuple
del numbers
