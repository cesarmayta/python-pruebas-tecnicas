"""
3. Given the following function:

def foo():
print("Inside my function")
  
Write a decorator that prints the message “Inside my decorator” before the message of the foo() function. 
"""

def mydecorator(funcMain):
    def funcion_decorador(*args,**kwargs):
        print("Inside my decorator")
        funcMain()

    return funcion_decorador

@mydecorator
def foo():
    print("Inside my function")

foo()
