"""
Python TUPLE - Pack, Unpack, Compare, Slicing, Delete, Key
"""

tuple = ("navin", "aryan", 9)

# empty tuple
emptyTuple = ()

# For writing tuple for a single value
singleElementTuple = (50,)

"""
select element from tuple
"""
tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida')
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(tup1[0:3])
print(tup1[:4])
print(tup1[2])

"""
Packing and Unpacking
In packing, we place value into a new tuple while in unpacking we extract those values back into variables.
"""
x = ("Guru99", 20, "Education")  # tuple packing
(company, emp, profile) = x  # tuple unpacking
print(company)
print(emp)
print(profile)

"""
Comparing tuples
"""
a = (5, 6)
b = (1, 4)
if a < b:
    print("a is less than b")
else:
    print("b is less than a")

"""
Deleting Tuples

Tuples are immutable and cannot be deleted, but deleting tuple entirely is possible by using the keyword
"""
tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida')
del (tup1)

"""
Slicing of Tuple
"""
x = ("a", "b", "c", "d", "e")
print(x[2:4])

"""
Built-in functions with Tuple

built-in functions like all(), any(), enumerate(), max(), min(), sorted(), len(), tuple(), etc.
"""
