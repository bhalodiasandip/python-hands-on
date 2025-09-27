#### 1. Pythonic Idioms & Best Practices
## 1.1 Truthy & Falsy Values

## instead of do below code
# if len(my_list) != 0:
#     print("Not empty")

## Pythonic
# if my_list:
#     print("Not empty")
##  Empty lists, dicts, sets, 0, None, False → all evaluate to False.

## 1.2 Multiple Variable Assignment
# a,b = 10,15
# a,b = b,a # swap without temp variable
# print(a)

### 1.3 List Comprehensions vs Loops
##Instead of:
# squares = []
# for x in range(5):
#     squares.append(x**2)

## Pythonic
# squares = [v ** 2 for v in range(4)]

## Also works with conditions:
# squares = [v ** 2 for v in range(4) if v % 2 == 0]

### 1.4 Dictionary & Set Comprehensions
# words = ["apple", "banana", "cherry"]
# lengths = {word: len(word) for word in words}
# print(lengths)
# chrs = {chr for word in words for chr in word}
# print(set(sorted(chrs)))


#### 2. Iterators, Generators & Lazy Evaluation
### 2.1 enumerate instead of range(len(...))
# for i,j in enumerate(["apple","bannana","cherry"]):
#     print(i, j)

#### 2.2 zip for Parallel Iteration
# k_list = ["0101114", "0101115", "0101116", "111111"]
# v_list = ["sandip", "ramesh", "anand", "devansh"]
# for k,v in zip(k_list,v_list):
#     print(k, v)

#### 2.3 Generators with yield
# def febbonacci(n):
#     a,b = 0,1
#     for _ in range(n):
#         yield a
#         a,b = b, a+b
# print(list(febbonacci(8)))

## difference between return and yield
## return → gives back a single value and ends the function immediately.
## yield → gives back one value but pauses the function, so it can continue next time.

### 2.4 Generator Expressions
## Below both works correctly. first because list and second becuase generator behaviour.
# sum_of_squares = sum([a ** 2 for a in range(6)])
# sum_of_squares = sum(a ** 2 for a in range(6))
# print(sum_of_squares)

#### 3. Functional Python

### 3.1 map, filter, reduce
# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x ** 2, nums)))
# print(list(filter(lambda x: x % 2 == 0, nums)))
# print(reduce(lambda x,y: x * y, nums))
####

### 3.2 any & all
# nums = [1, 2, 3, 0]
# print(any(nums))   
# # True (at least one truthy)

# print(all(nums))   
# # False (0 is falsy) : 0, False, "", None, empty array [] considered as false

#### 4. Advanced Data Structures
### 4.1 collections.Counter
# from collections import Counter
# fruits = ["apple","banana","cherry","apple","cherry","apple"]
# print(Counter(fruits))

### 4.2 defaultdict
# from collections import defaultdict
# d = defaultdict(list)
# d["fruits"].append("apple")

## Normaly it gives KeyError: 'fruits' because "fruits" key does not exist yet.
## But here it works because we use defaultdict(list).
## so If I try to access a missing key, automatically create it with a default value of list().
## defaultdict(int) → default value 0
## defaultdict(list) → default value [] (an empty list)
## defaultdict(str) → default value ""
 

### 4.3 namedtuple
# from collections import namedtuple
# MyPointClass = namedtuple("Point", ['x', 'y'])
# ## field_names (str or list)
# ## The names of the attributes.
# ## Can be given as:
# ## A space/comma-separated string: "x y" or "x, y"
# ## A list of strings: ["x", "y"]
# A = MyPointClass(2.5, 9.6)
# print(A.x, A.y)

### 4.4 deque
# from collections import deque
# dq = deque(['a', 'b', 'c'])
# dq.appendleft('d')
# ## deque means double ended queue. you can append and pop from both end. 
# ## In this way it is different from normal list.
# ## with normal list insert(0, x) or pop(0) (from left) are O(n) → slow for big lists.
# ## With deque, both left and right operations are O(1) → very fast.
# print(dq) 
# dq.pop()
# print(dq)

#### 5. Context Managers (with)

### 5.1 Context Managers (with)
# with open("data.txt", "r") as f:
#     data = f.read()
#     print(data)

### 5.2 Custom Context Manager
# class MyContaxt:
#     def __enter__(self):
#         print("Enter in class")
#         return self
#     def greet(self):
#         print(f"Hello")
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exit block")
# with MyContaxt() as ctx:
#     ctx.greet()        
# ## __enter__ Called automatically when the block start
# ## __exit__ Called automatically when the with block ends.
# ## It always runs:
# ## Even if no error happened.
# ## Even if an exception happened inside the block.
# ## Parameters:
# ## exc_type → exception type (if any)
# ## exc_val → exception instance (if any)
# ## exc_tb → traceback object (if any)    
# ## Context managers are used for setup and cleanup logic:
# ## Opening/closing files
# ## Acquiring/releasing locks
# ## Connecting/disconnecting from databases
# ## Starting/closing network sessions

#### 6. Decorators
### 6.1 Simple Decorator
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
# @logger
# def greet(name):
#     print(f"Hello {name}")
# greet("Sandip")    

##logger is a decorator that adds behavior (logging) before running a function.
##@logger automatically applies it to greet.
##This is how Python decorators allow code reusability (adding extra functionality without changing the original function).

### 6.2 Decorator with Arguments
# def sandip_repeat(n):
#     def sandip_decorator(func):
#         def sandip_wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, ** kwargs)
#         return sandip_wrapper
#     return sandip_decorator
# @sandip_repeat(5)
# def say_hi(name):
#     print(f"Hi {name}")
# say_hi("Shiv")    

#### 7. Advanced *args & **kwargs
# def demo(a, *args, **kwargs):
#     print(f"var a: {a}")
#     print(f"var arguments: {args}")
#     print(f"var keyword arguments: {kwargs}")
# demo(5, 6,7,8,name="sandip",age=40)    

#### 8. Dunder (Magic) Methods
# class Vector:
#     def __init__(self, x, y):
#         self.x, self.y = x,y
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#     def __repr__(self):
#         return f"Vector Object with: {self.x} and {self.y}"
# v1 = Vector(2,5)
# v2 = Vector(7,9)
# print(v1 + v2)
### let’s compare __repr__ vs __str__ clearly:
### __repr__ Official/unambiguous string representation (for developers/debugging).
### __str__ Informal/readable string representation (for users).
### For example. print(obj) __str__ (if exists case), __repr__ (to handle Non exists case)

#### 9. Custom Iterator
### An iterator is an object in Python that allows you to traverse through all the elements of a collection (like a list, tuple, or dictionary) one by one, without needing to know the internal structure.
### Think of it like a bookmark: it remembers your current position while looping.
### You can get the next item using next().
### Iterators implement two methods:
### __iter__() → returns the iterator object itself.
### __next__() → returns the next item. Raises StopIteration when there are no items left.

# class MyRange:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if(self.current >= self.end):
#             raise StopIteration #REMEMBER raise keyword
#         value = self.current
#         self.current += 1
#         return value
    
### case 1: check above iterator with loop    
# num = MyRange(1,5)
# for n in num:
#     print(n)

### case 2: check above iterator with next
### Before execute below example please comment above loop otherwise point will not be reset position.

# print(next(num))
# print(next(num))
# print(next(num))

###Converting Iterable to Iterator
# m_list = [1,5,8,9]
# it = iter(m_list)
# print(next(it))
# print(next(it))
# print(next(it))