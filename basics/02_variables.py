# A variable is a container for a value, which can be of various types

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
  - Can have numbers but can not start with one
"""

# Declare the variable & initilize it
age = 24
name = "Aakrit Subedi"
marks = 69.69
isMale = True

print("Name " + name)
print("Age %i" % (age))
print("Marks %f" % (marks))
print("Male %s" % (isMale))

# Python Numbers
'''
There are three numeric types in Python:
- int
- float
- complex
'''
# Variables of numeric types are created when you assign a value to them:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Python Strings
# Strings in python are surrounded by either single quotation marks, OR double quotation marks.
print("Aakrit")
print('Aakrit')
fullName = 'Aakrit Subedi'
print('My name is %s' % (fullName))
link = "https://www.w3schools.com/python/python_strings_methods.asp"
print('Checkout the link %s to learn about string methods in Python' % (link))

# Python Booleans
'''
Booleans represent one of two values: True or False.

Almost any value is evaluated to True if it has some sort of content. 
- Any string is True, except empty strings.
- Any number is True, except 0.
- Any list, tuple, set, and dictionary are True, except empty ones.

In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
'''

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return.
print(bool("Hello"))
print(bool(15))
