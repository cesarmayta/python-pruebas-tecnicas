"""
Given a list of strings, write a function that prints a reverse version of each string:

For example:
>A = [ "Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]
>magic_function(A)
['dlroW olleH', 'nohtyP olleH', '8 7 6 5 4 3 2 1']
"""
def magic_function(listA):
    listB = []
    for valA in listA:
        for i in range(length(valA),0,-1):
            strB += i
        listB.append(strB)
    return listB