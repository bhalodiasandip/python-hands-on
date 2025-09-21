from math import sqrt
#### Function Annotations & Type Hints
# def pythagoras_number(a: float, b:float) -> float:
#     return sqrt((a ** 2) + (b ** 2))
# a = 12
# b = 5
# result = pythagoras_number(a,b)
# print(f"Pythagoras of {a} and {b} is: {result}")

#### Default Parameters
# def greet(name: str = "sandip") -> str:
#     return f"Hello {name}"
# print(greet())
# print(greet("Devansh"))

#### Keyword Arguments
# def student(name, age):
#     return f"{name}: Age {age}"
# print(student(age=40, name="Sandip"))


#### Arbitrary Arguments
# *args (tuple of extra positional arguments)
# **kwargs (dict of extra keyword arguments)

# def my_func(*args, **kwargs):
#     print(args)     #Tuple
#     print(kwargs)   #Dict 
# my_func(2,"raja",True, localname="Mohan", age=42)


#### Local vs Global variable.
# x = 10  # global
# def func():
#     x = 5  # local
#     print("Inside:", x)
# func() #"Inside:5"
# print("Outside:", x) #"Outside:10"

# x = 10
# def update():
#     global x
#     x = 20
# update()
# print(x)  # 20   ## To update global variable inside function use "global" keyword

#### Lambda (Anonymous) Functions
# square = lambda x : x ** 2
# print(square(5))

#### Higher-Order Functions
# def apply(func, x): 
#     return func(x)
# def double(x): 
#     return 2 * x
# print(apply(double, 5))

#### map, filter, and reduce
# from functools import reduce
# nums = [1,2,3,4]
# print(list(map(lambda x: x ** 2, nums)))
# print(list(filter(lambda x : x % 2 == 0, nums)))
# print(reduce(lambda a,b: a+b, nums)) #Output:  10
# print(reduce(lambda a,b: a + b, range(1,101)))
# reduce function you pass to reduce() must take exactly two arguments. here a,b
# reduce() works by taking two items at a time from your iterable and combining them.
# The result of each step becomes the first argument (a) in the next step, 
# and the next element from the iterable becomes the second argument (b).

#### Recursion
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

#### Function Annotations & Type Hints
# def add(a: int, b: int) -> int: #type hint gives IDE auto suggestion inside function body
#     return a + b

#### Docstrings
## doc string act as a documentation for the function. i.e what function do?, purpose of function.
# def greet():
#     """This function prints a greeting message"""
#     print("Hello")

# print(greet.__doc__) # This function prints a greeting message

#### *args vs **kwargs Deep Dive
# def demo(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
# demo(1, 2, 3, 4, 5, x=10, y=20)

#### Decorators (Interview Favorite)
# Decorator = A function that takes another function and adds extra behavior without modifying it.

# def my_decorator(func):
#     def my_wrapper():
#         print("Before Function")
#         func()
#         print("After function")
#     return my_wrapper

# @my_decorator
# def say_hello():
#     print("Hello")
# say_hello()

# @my_decorator
# def say_world():
#     print("World")
# say_world()    
## Before Function
## Hello
## After function
## Before Function
## World
## After function

####
# Used to modify variables in the enclosing (but not global) scope.
# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x += 5
#         print(x)
#     inner()
# outer()

#### When use lamda function
# when you don’t plan to reuse the function.Like map, filter, sorted, and reduce.

####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
