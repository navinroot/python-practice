"""
Python For & While Loops: Enumerate, Break, Continue Statement
"""


# while loop
def whileLoopTest():
    x = 0
    while x < 4:
        print(x)
        x += 1


whileLoopTest()

"""
for loop test
"""


def forLoopTest():
    print("for loop test")
    for x in range(2, 9):
        print(x)


forLoopTest()

"""
for loop for string
"""


def forLoopForString():
    print("for loop test for String")
    month = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for m in month:
        print(m)


print(forLoopForString())

"""
break statement in for loop
"""


def forLoopForStringWithBreak():
    print("for loop test for String with break")
    month = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for m in month:
        if (m == "Feb"): break
        print(m)


forLoopForStringWithBreak()

"""
continue statement in for loop
"""


def forLoopForStringWithContinue():
    print("for loop test for String with Continue")
    month = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for m in month:
        if (m == "Feb"): continue
        print(m)


forLoopForStringWithContinue()

"""
use "enumerate" function for "For Loop"
Enumerate function in "for loop" does two things

It returns the index number for the member
And the member of the collection that we are looking at
"""


def forLoopForStringWithEnumerate():
    print("for loop test for String with Enumerate")
    month = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for i, m in enumerate(month):
        print(i, m)


forLoopForStringWithEnumerate()
