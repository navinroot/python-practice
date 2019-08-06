"""
Python Dictionary(Dict): Update, Cmp, Len, Sort, Copy, Items, str Example

Dictionaries are another example of a data structure. A dictionary is used to map or associate things you want to store
the keys you need to get them. A dictionary in Python is just like a dictionary in the real world. Python Dictionary are
 defined into two elements Keys and Values.

Keys will be a single element
Values can be a list or list within a list, numbers, etc.

There are two important points while using dictionary keys

1. More than one entry per key is not allowed ( no duplicate key is allowed)
2. The values in the dictionary can be of any type while the keys must be immutable like numbers, tuples or strings.
3. Dictionary keys are case sensitive- Same key name but with the different case are treated as different keys in Python
 dictionaries.
"""

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 28, 'Robert': 25}
print(Dict['Tiffany'])

"""
Copying dictionary
You can also copy the entire dictionary to new dictionary. 
For example, here we have copied our original dictionary to new dictionary name "Boys" and "Girls".
"""

Boys = {'Tim': 18, 'Charlie': 12, 'Robert': 25}
Girls = {'Tiffany': 22}
studentX = Boys.copy()
studentY = Girls.copy()
print(studentX)
print(studentY)

"""
Updating Dictionary
You can also update a dictionary by adding a new entry or a key-value pair to an existing entry or by deleting an 
existing entry. Here in the example we will add another name "Sarah" to our existing dictionary.
"""

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Dict.update({"Sarah": 9})
print(Dict)

# delete an element
del Dict['Charlie']
print(Dict)

"""
Dictionary items() Method

The items() method returns a list of tuple pairs (Keys, Value) in the dictionary.
"""
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("Students Name: %s" % list(Dict.items()))

"""
Check if a given key already exists in a dictionary
"""
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
keyCheck = 'Tim'
if keyCheck in Dict.keys():
    print(keyCheck, 'is present')
else:
    print(keyCheck, 'is not present')

"""
Sorting the Dictionary
"""
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Boys = {'Tim': 18, 'Charlie': 12, 'Robert': 25}
Girls = {'Tiffany': 22}
Students = list(Dict.keys())
Students.sort()
for S in Students:
    print(":".join((S, str(Dict[S]))))

"""
Dictionary len() Method
The len() function gives the number of pairs in the dictionary.
"""
print("length of dictionary = ", len(Dict))

"""
Variable Types
Python does not require to explicitly declare the reserve memory space; it happens automatically. The assign values to
 variable "=" equal sign are used. The code to determine the variable type is " %type (Dict)."
"""

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("variable Type: ", type(Dict))

"""
Dictionary Str(dict)
With Str() method, you can make a dictionary into a printable string format.
"""
print(Dict)
print(str(Dict))
