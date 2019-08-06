"""
Python Functions Examples: Call, Indentation, Arguments & Return Values

"""


# varargs in python function
def square(x):
    return x * x


print(square(2))


# default argument in function
def sum2(x, y=2):
    return x + y


print(sum2(3, 2))
print(sum2(3))

# passing named argument
print(sum2(y=2, x=9))


# varargs arguement in function
def varArgsFunction(*args):
    print(args)


varArgsFunction(1, 2, 3, 4, 5, 6)
