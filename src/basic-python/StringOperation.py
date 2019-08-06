"""
Python does not support a character type, these are treated as strings of length one, also considered as substring.

We use square brackets for slicing along with the index or indices to obtain a substring.
"""
str1 = "navin"
str2 = "navinaryan"
print("str1[0]: ", str1[0])
print("str2[1:6]: ", str2[1:6])

"""
in -> checks if a substring is present in a string
"""
if 'na' in str1:
    print("na is present in str: ", str1)

"""
not in -> opposite of in
"""
if 's' not in str1:
    print("sr is not present in str: ", str1)

"""
+ -> concats to string
"""
str3 = str1 + str2
print("concat str1+str2 =", str3)

"""
* -> repeat string n number of times
"""
print("* operator use case = str1*2=", str1 * 2)

"""
Python String replace() Method
"""
oldstring = 'I like coding'
newstring = oldstring.replace('like', 'love')
print(newstring)

"""
Changing upper, lower and capitalize case strings
"""
string = "coding in python"
print(string.upper())
print(string.capitalize())
print(string.lower())

"""
Using "join" function for the string
"""
print(":".join("Python"))

# Reversing String
string = "12345"
print(''.join(reversed(string)))

# Split Strings
word = "python career python"
print(word.split(' '))
word = "python career python"
print(word.split('p'))
x = "python"
x.replace("python", "Python")
print(x)
x = "python"
x = x.replace("python", "Python-3.6")
print(x)
