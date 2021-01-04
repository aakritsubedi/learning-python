# A List is a collection which is ordered and changeable. Allows duplicate members. 
'''
Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
'''
# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# use a constructor
vegitables = list(('Cauliflower', 'Potato', 'Broccoli', 'Cabbage'))

print(numbers)
print(fruits)
print(vegitables)

# Get a value
print(fruits[1])
print(vegitables[2])

# Get the last value
print(fruits[-1])
print(vegitables[-1])

# Get length
print(len(fruits))
print(len(vegitables))

# Append to list
fruits.append('Mangos')
vegitables.append('Spanich')
print("Updated List: ")
print(fruits)
print(vegitables)

# Remove from list
fruits.remove('Grapes')
# fruits.remove('Banana') ValueError: list.remove(x): x not in list

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Change value
fruits[0] = 'Blueberries'
print(fruits)

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

# Loop in list 
for fruit in fruits:
  print(fruit)
