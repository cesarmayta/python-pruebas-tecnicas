"""
2. Given a list of strings, write a function that prints a reverse version of each string:

For example:
>A = [ "Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]
>magic_function(A)
['dlroW olleH', 'nohtyP olleH', '8 7 6 5 4 3 2 1']
"""
def reverse_function(listA):
    listReverse = [x[::-1] for x in listA]
    return listReverse

A = [ "Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]
B = reverse_function(A)
print(B)