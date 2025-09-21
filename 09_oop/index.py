#### Introduction to OOP
# Encapsulation (data hiding)
# Inheritance (reuse code in subclasses)
# Polymorphism (same interface, different behavior)


#### Classes and Objects
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello {self.name} You are {self.age} Years Old.")
# student1 = student("Rajesh", 45)
# student1.greet()
## Here note that we no need to declare variable like PHP.
## They are created dynamically when you assign to them, usually inside __init__.

#### Instance vs Class Variables
# class Company:
#     isISO = False
#     def __init__(self, name):
#         self.name = name
#     def setIso(self, isoValue:bool):
#         self.isISO = isoValue
#     def greet(self):
#         print(f"Company {self.name} is ISO Certified: {'Yes' if self.isISO else 'No'}")

# c1 = Company("Silvertouch")
# c1.setIso(True)


#### Instance, Class, and Static Methods
# class myclass:
#     name = "Chiru"
#     def greet(self, name):
#         self.name = name
#         print(f"name is: {self.name}")
#     @classmethod
#     def about(cls):
#         print("class Mehotd: ", cls)
#     @staticmethod
#     def utility():
#         print("This method to use utility or function library that not depends on class or object")
# c1 = myclass()
# c1.greet("Hari")
# c1.about()
# c1.utility()

#### Encapsulation
##Encapsulation = hiding internal data by using private/protected attributes.
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     def deposit(self, amount):
#         self.__balance += amount
#     def withdraw(self, amount):
#         self.__balance -= amount
#     def get_amount(self):
#         print(f"Amount is: {self.__balance}")
# a = BankAccount(1000)
# a.deposit(700)
# a.withdraw(200)
# a.get_amount()
# print(a.__balance) # error: __balance cannot be accessed directly
###_single_underscore (protected)
###__double_underscore (private / name mangled)


#### Inheritance
# class Animal:    
#     _numberOfLegs = 4
#     __canwalk = False
#     def speak(self):
#         print("Animal can speak")    
# class Dog(Animal)    :
#     def describe(self):
#         print(f"Dog can bark and it has {self._numberOfLegs}")

# class Man(Animal):    
#     _numberOfLegs = 2
#     def describe(self):
#         print(f"Man can speak and it has {self._numberOfLegs}")
#     def canwalk(self):
#         print(f"Man can speak and it has {self.__canwalk}")
# # d = Dog  # without bracket Dog is not object it is class itself.
# d = Dog()
# d.describe()
# m = Man()
# m.describe()
# m.canwalk() #Error. can't access private property __canwalk in this method.

#### Method overriding using super
# class Animal:
#     def speak(self):
#         print("Animal can speak")
# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("Dog speak Wow")
# d = Dog()
# d.speak()


#### Multiple Inheritance
#### Python support Multiple Inheritance unlike PHP
# class machine:
#     def move(self):
#         print("Move Mechenically")
# class human:
#     def move(self):
#         print("Move Biologically")
# class MovableEntity(machine, human):
#     pass
# me = MovableEntity()
# me.move() # Resolves using MRO (Method Resolution Order) 
# ### Move Mechenically
# print(MovableEntity.mro()) #this will give sequence of priority list by resolution order.


#### Polymorphism
#### Polymorphism allows different classes to respond to the same method name in their own way.
# class Cat:
#     def speak(self):
#         print("Meau")
# class Dog:
#     def speak(self):
#         print("Wow")
# for animal in [Cat(), Dog()]:
#     animal.speak()

#### Dunder (Magic) Methods
#### Dunder = Double UNDerscore, like __init__, __str__, __eq__, __add__, __len__
#### __init__ is constructor method for python
#### __str__ automatically call when print object like print(obj)
#### __eq__ automatically call when compare object like if(obj1 == obj2)
#### __add__ automatically call when add two objects like obj1 + obj2
#### __len__ automatically call when call of len method for object like len(obj)
# import math
# class City:
#     def __init__(self, name, lat, long):
#         self.name, self.lat, self.long = name, lat, long
#     def __str__(self):
#         return f"city name: {self.name} and its position is: {self.lat, self.long}"
#     def __eq__(self, other):
#         return (self.lat == other.lat) and (self.long == other.long)
#     def __add__(self,other):
#         return City(self.name, self.lat + other.lat, self.long + other.long) 
#     def __len__(self):
#         return int(2 * math.pi * self.lat * self.long)
# c1 = City("Rajkot", 10.5, 2.8)
# print(c1)
# c2 = City("Kathiyawad", 10.5, 2.8)
# c3 = City("Ahmedabad", 11.5, 3.6)

# ### In below example while comparing c1 == c2 it calls __eq__ automatically
# print(f"{c1.name} and {c2.name} are Same" if c1 == c2 else f"{c1.name} and {c2.name} are Different")
# print(f"{c1.name} and {c3.name} are Same" if c1 == c3 else f"{c1.name} and {c3.name} are Different")

# ### In below example while adding c1 + c3 it calls __add__ automatically
# c4 = c1 + c3
# print(c4)

# ### In below example while call len function it calls __len__ automatically
# print(len(c1))

#### Composition for (has-a relation) and Inheritance for (is-a relation)
#### Sometimes we need to use composition instead of inheritance. like below..
# class Engine:
#     def start(self):
#         print("Engine is starting..")
# class Car:
#     def __init__(self):
#         self.engine = Engine() #has-a relation
#     def start(self):
#         self.engine.start()
#         print("Car is starting")
# c = Car()
# c.start()

#### Abstract Classes (abc module)
#### here abc stands for "Abstract class"
#### Abstract classes can’t be instantiated.
#### Subclasses must implement abstract methods.
# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self): pass        

# class car(vehicle):
#     def __init__(self, name):
#         self.name = name
#     def start(self):
#         print(f"{self.name} is starting")
# c = car("BMW")
# c.start()    


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
