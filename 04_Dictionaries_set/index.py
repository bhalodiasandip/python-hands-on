my_dict = {} #create empty dir

# With initial values
# person = {
#     "name": "Alice",
#     "age": 25,
#     "is_student": False
# }
# print(person['name'])
# print(person.get('age'))
# print(person.get('city')) # None (no error if key is missing)

# #Adding & updating entries
# person['city'] = 'Delhi'
# person['age'] = 40
# print(person)

#Deleting entries
# del person['city']
# print(person)

# removed = person.pop('age')
# print(removed)

#Dictionary methods
# print(person.keys()) #return key list
# print(person.values()) #reterun values list
# print(person.items()) #return list of tuples(key,value)
# person.clear() #Empty dictionary
# print(person)

##Iterating over dictionaries
# for key in person:
#     print(key, person[key])

# for key,value in person.items():
#     print(key, value)

# for m in person.items():
#     print(m[1])    

# Dictionary comprehension
# squares = {x: x ** 2 for x in range(5)}
# print(squares)

# Interview Tips
# Keys must be hashable (immutable).
# Dictionary lookup is O(1) on average (hash table). 
# O(1) means constant time: the time it takes does not grow as the dictionary gets bigger.
# Use .get() or in to check key existence safely.
# dict is unordered before Python 3.7; from 3.7+, insertion order is preserved (but don’t rely on it for logic).

my_set = {1, 2, 3}
# empty_set = set()  # NOT {} (that’s a dict)
# print(empty_set)
# my_set.add(4)
# my_set.remove(2)   # KeyError if not present
# my_set.discard(5)  # No error if missing
# print(my_set)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)   # Union        {1, 2, 3, 4, 5}
# print(a & b)   # Intersection {3}
# print(a - b)   # Difference   {1, 2}
# print(a ^ b)   # Symmetric difference {1, 2, 4, 5}

# print(3 in my_set)
# for x in my_set:
#     print(x)

# frozenset
fs = frozenset([1, 2, 3])
fs.add(4)  # ❌ error - immutable

# Use case of frozenset
# When you want a set of values that cannot be changed later.
# When you need to use a set as a key in a dictionary or as an element of another set (because only hashable objects can be keys).
# Think of it like this:
# A set is a bag of unique items (no duplicates, order doesn’t matter), but it is mutable (you can add/remove elements).
# Mutable things can’t be used as dictionary keys or put inside other sets because they can change (which would break hashing).

#below will give type error
# skills_to_role = {
#     {'python', 'django'}: 'Backend Developer'   # <-- set is unhashable
# }
# Error: TypeError: unhashable type: 'set'

# Solution: Use frozenset
# skills_to_role = {
#     frozenset(['python', 'django']): 'Backend Developer',
#     frozenset(['python', 'pandas']): 'Data Analyst'
# }

# print(skills_to_role[frozenset(['django', 'python'])])
# Output: Backend Developer  ✅ order doesn’t matter

# # Suppose you want to store unique groups of fruits
# groups = set()

# groups.add(frozenset(['apple', 'banana']))
# groups.add(frozenset(['banana', 'apple']))  # same group, won't duplicate
# groups.add(frozenset(['apple', 'cherry']))

# print(groups)
# # {frozenset({'apple','banana'}), frozenset({'apple','cherry'})}

