def function(num,*args):
    print(num)
    print(args)
function(1, 2, 3, 4, 5)    

""" 
 Here i am using *args and.
 *args is used to pass any number of arguments to the function.
 *args is a tuple.
 Output:
    1
    (2, 3, 4, 5)
 Here 1 is printed as num and (2, 3, 4, 5) is printed as args.   
"""



def function1(num,**kwargs):
    print(num)
    print(kwargs)    
function1(1, a=2, b=3, c=4, d=5)

"""
Here i am using **kwargs.
**kwargs is used to pass any number of keyword arguments to the function.
**kwargs is a dictionary.
Output:
    1
    {'a': 2, 'b': 3, 'c': 4, 'd': 5}
Here 1 is printed as num and {'a': 2, 'b': 3, 'c': 4, 'd': 5} is printed as kwargs.

"""    