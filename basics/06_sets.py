# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits)

# Add to set
fruits.add('Grape') # set(['Mango', 'Grape', 'Apples', 'Oranges'])

# Remove from set
fruits.remove('Grape') # set(['Mango', 'Apples', 'Oranges'])

# Add duplicate
fruits.add('Apples') # not allowed

# Clear set
fruits.clear() # set([])

# Delete
del fruits

print(fruits) # name fruits is not defined
