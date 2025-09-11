# fruits = ["apple","banana","cherry","grapes"]
# print(fruits[1])
# print(fruits[-1])
# print(fruits[-2])

# numbers = [10, 20, 30, 40, 50]
# print(numbers[1:3])
# print(numbers[2:])
# print(numbers[:3])
# print(numbers[0::2])
# print(numbers[::-1])

# fruits = ["apple", "banana", "cherry"]

# fruits[1] = 'kiwi'
# print(fruits)

# fruits.append("grapes")
# print(fruits)

# fruits.insert(1, "orange")
# print(fruits)

# fruits.remove("kiwi")
# print(fruits)

# last = fruits.pop()
# print(last)
# print(fruits)

# del fruits[1]
# print(fruits)

### Useful List Functions
# nums = [4, 2, 9, 7, 2, 9]
# print(max(nums))
# print(min(nums))
# print(len(nums))
# print(nums.count(9))

# nums.sort()
# print(nums)

# nums.reverse()
# print(nums)

# figures = [0,1,2,3,4,5,6,7,8]
# result = []
# for i,f in enumerate(figures):
#     # result.append(f ** 2)
#     result += [f ** 2]
# print(result)

### Here is the short method of above to add directly while looping
# result = [f**2 for f in figures]
# print(result)

### apply condition
# result = [f**2 for f in figures if f % 2 == 0]
# print(result)

########## TUPLE ############
# t = ()
# print(t) # Empty tuple

# colors = ("red","greeen","blue")
# print(colors)
# print(colors[1]) # green
# colors[1] = 'yellow' #error, tuples are immutable.

# teams = ('aus',) 
#single element must include comma. 
#otherwise python not treat as tuple. instead it treat as string in this case

##Tuple Packing & Unpacking
# person = ("John", 40, "Programmer")
# name, age, job = person
# print(job) #Programmer

# nums = (4, 2, 9, 7, 2)
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(nums.count(2))
# print(nums.index(9))

#Q1: Create a list of 3 cities and print the last city using negative indexing.
# cities = ["rajkot","bombay","delhi"]
# print(cities[-1])

# Q2: From a list [1,2,3,4,5,6], generate a new list containing only even numbers using list comprehension.
# result = [i for i in range(7) if i % 2 == 0]
# print(result)


# Q3: Convert a tuple into a list, add one element, and convert it back to a tuple.
# cities = ("rajkot","bombay","delhi")
# city_list = list(cities)
# city_list.append("Ahmedabad")
# print(city_list)
# print(tuple(city_list))


##Q.4 How do you remove duplicates from a list?
# mylist = [1, 2, 2, 3, 4, 4]
# myunique = list(set(mylist))
# print(myunique)