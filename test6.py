"""
Given the following function:

def foo():
print("Inside my function")
  
Write a decorator that prints the message “Inside my decorator” before the message of the foo() function.
"""

def mydecorator(myFunction):

    def functionDecorator():
        print("Inside my decorator")
        
        myFunction()

    return functionDecorator

@mydecorator
def foo():
    print("Inside My Function")

foo()