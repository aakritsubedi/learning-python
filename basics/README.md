# Learning Python

## Basics

### Introduction 
Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace.  

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991. It is used for:
- web development (server-side),
- software development,
- mathematics,
- system scripting ...

Q. What can Python do?  
- Python can be used on a server to create web applications.
- Python can be used alongside software to create workflows.
- Python can connect to database systems. It can also read and modify files.
- Python can be used to handle big data and perform complex mathematics.
- Python can be used for rapid prototyping, or for production-ready software development.  

Q. Why Python?
- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-oriented way or a functional way.

**Python Syntax compared to other programming languages**
- Python was designed for readability, and has some similarities to the English language with influence from mathematics.
- Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

```python
print("Let's Start!")
```

### Python Install
Many PCs and Macs will have python already installed. To check if you have python installed on a Linux or Mac, then on linux open the command line or on Mac open the Terminal and type:

```shell
$ python --version
```

### The Python Command Line
To test a short amount of code in python sometimes it is quickest and easiest not to write the code in a file. This is made possible because Python can be run as a command line itself.  
Type the following on the Windows, Mac or Linux command line:  

```shell
$ python
```
Or, if the "python" command did not work, you can try "py".  

From there you can write any python. Let us print hello world.
```shell
print('Hello World')
```
Which will write "Hello, World!" in the command line. 

Whenever you are done in the python command line, you can simply type the following to quit the python command line interface:

```shell 
exit()
```
[Example: Hello World](../basics/01_helloWorld.py)

### Variables
Variables are containers for storing data values.

Creating Variables: 
```python
name = "Aakrit Subedi"
age = 24
print(name)
print(age)
```
**Note:** Variables do not need to be declared with any particular type, and can even change type after they have been set. 

```python
age = 24 # age is of type int
age = "Twenty Four" # age is of type str
print(age) # Twenty Four
```
[Example: Variables](../basics/01_helloWorld.py/02_variables)

### Data types
Built-in Data Types
In programming, data type is an important concept. Variables can store data of different types, and different types can do different things.  
Python has the following data types built-in by default, in these categories:
- **Text Type:**	str
- **Numeric Types:**	int, float, complex
- **Sequence Types:**	list, tuple, range
- **Mapping Type:**	dict
- **Set Types:**	set, frozenset
- **Boolean Type:**	bool
- **Binary Types:**	bytes, bytearray, memoryview

You can get the data type of any object by using the type() function:
```python
x = 5
print(type(x)) # <class 'int'>
```

### Casting 
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.  
Casting in python is therefore done using constructor functions:

- `int()`: constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
- `float()`: - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
- `str()`: - constructs a string from a wide variety of data types, including strings, integer literals and float literals  

[Example: Casting](../basics/03_casting.py)

### Python Collections (Arrays)
There are four collection data types in the Python programming language:

- **List** is a collection which is ordered and changeable. Allows duplicate members.
- **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.
- **Set** is a collection which is unordered and unindexed. No duplicate members.
- **Dictionary** is a collection which is unordered and changeable. No duplicate members. 

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

#### Lists 
Lists are used to store multiple items in a single variable.   
Lists are created using square brackets:
```python 
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# use a constructor
vegitables = list(('Cauliflower', 'Potato', 'Broccoli', 'Cabbage'))
```
- **Ordered** The python lists are ordered, it means that the items have a defined order, and that order will not change. 
- **Changeable** The list is changeable, meaning that we can change, add, and remove items in a list after it has been created. 
- **Allow Duplicates** The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

A list can contain different data types:

```python
randomList = ["Aakrit Subedi", 24, True, 69.69, "male"]
print(type(randomList)) # <class 'list'>
```
[Example: Lists](../basics/04_lists.py)

#### Tuples
Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. 
```python
fruits = ("apple", "banana", "cherry")
# use a constructor
numbers = tuple((1,2,3,4,5,6,7,8,9))
```
- **Ordered** The tuples are ordered, it means that the items have a defined order, and that order will not change.
- **Unchangeable** Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
- **Allow Duplicates** Since tuple are indexed, tuples can have items with the same value.

**Note:** Tuple items can be of any data type and can contain different data types.
```python
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
```

[Example: Tuples](../basics/05_tuples.py)

#### Sets
Sets are used to store multiple items in a single variable. A set is a collection which is both unordered and unindexed. Sets are written with curly brackets.
```python
myset = {"apple", "banana", "cherry"}
```
- **Unordered** Unordered means that the items in a set do not have a defined order. Set items can appear in a different order every time you use them, and cannot be referred to by index or key. 
- **Unchangeable** Sets are unchangeable, meaning that we cannot change the items after the set has been created.
- **Duplicates Not Allowed** Sets cannot have two items with the same value.

**Note:** Sets items can be of any data type and can contain different data types.
```python
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
```

[Example: Tuples](../basics/06_sets.py)

#### Dictionaries 
Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is unordered, changeable and does not allow duplicates. Dictionaries are written with curly brackets, and have keys and values:
```python 
myInfo = {
  "name": "Aakrit Subedi",
  "college": "Kantipur Engineering College",
  "dob": "1996-04-09"
}
print(myInfo)
```
- Dictionary items are unordered, changeable, and does not allow duplicates. 
- Dictionary items are presented in key:value pairs, and can be referred to by using the key name. 
```python 
print(myInfo["name"]) # Aakrit Subedi
print(myInfo["college"]) # Kantipur Engineering College
```

[Example: Tuples](../basics/07_dictionaries.py)
