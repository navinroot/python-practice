# Python Variables: Declare, Concatenate, Global & Local

# declare a variable ( it's global variable)
a = "global variable"
print(a)


# declare local variable
def fun():
    a = "local variable"
    print(a)


fun()
# here global variable a is not changing, printing global variable after method closure
print(a)


# access global variable and change global variable inside function
def accessAndChangeGlobalVariable():
    global a
    print("printing global variable inside local function, a= ", a)
    a = "changed global variable inside local function"


accessAndChangeGlobalVariable()
print(a)
