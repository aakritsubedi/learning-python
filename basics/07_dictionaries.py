# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
myInfo = {
    'first_name': 'Aakrit',
    'last_name': 'Subedi',
    'age': 24
}

# Use constructor
# myInfo2 = dict(first_name='Aakrit', last_name='Subedi')

# Get value
print(myInfo['first_name'])
print(myInfo.get('last_name'))

# Add key/value
myInfo['phone'] = '555-555-5555'

# Get dict keys
print(myInfo.keys())

# Get dict items
print(myInfo.items())

# Copy dict
myInfo2 = myInfo.copy()
myInfo2['city'] = 'Kathmandu'

# Remove item
del(myInfo['age'])
myInfo.pop('phone')

# Clear
myInfo.clear()

# Get length
print(len(myInfo2))

# List of dict
people = [
    {'name': 'Aakrit Subedi', 'age': 24},
    {'name': 'John Doe', 'age': 25}
]

print(people[0]['name'])
print(people[1]['name'])
