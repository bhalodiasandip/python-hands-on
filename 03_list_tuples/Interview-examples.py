### Q1. Remove duplicates from a list while keeping order
# nums = [1, 2, 2, 3, 1, 4, 2]
# print(list(set(nums)))

# Q2. Find the second largest number in a list
# nums = [10, 40, 20, 50, 30]
# print(sorted(nums)[-2])

### Q3. Flatten a nested list (1 level)
# nested = [[1, 2], [3, 4], [5, 6]]
# print([g for i in nested for g in i])

### Q4. Reverse a list without using .reverse() or slicing
# nums = [1, 2, 3, 4]
# n =len(nums) - 1
# result = []
# while(n >= 0):
#     result += [nums[n]]
#     n -= 1
# print(result)

##Method - 2
# nums = [1, 2, 3, 4]
# result = []
# for i in nums:
#     result.insert(0, i)  # it insert every new item at 0 so other items slice moves one right.
# print(result)

### Q5. Count frequency of each element
# nums = [1, 2, 2, 3, 1, 4, 2]
# result = {}
# for i in nums:
#     result[i] = nums.count(i)
# print(result)    

#############Tuple practice#########
# Q6. Swap two variables using tuples
# a = 5
# b = 10
# b,a = (a,b)
# print(a)
# print(b)

# Q7. Unpack a tuple with unknown length using
# info = ("Alice", "Engineer", "NY", 25, "Python")
# name, post, *rest = info
# print(name) # Alice
# print(rest) # ['NY', 25, 'Python']

# Q8. Check if a tuple is hashable and usable as a dictionary key
# t1 = (1, 2, 3)
# t2 = ([1, 2], 3)

# t1 = (1, 2, 3)
# t2 = ([1, 2], 3)

#A tuple is hashable only if all its elements are also hashable.
# t1 works
# my_dict = {t1: "ok"}
# print(my_dict)           # {(1, 2, 3): 'ok'} int is hashable

# # t2 gives error
# my_dict = {t2: "error"}  # ❌ TypeError: unhashable type: 'list'

##Q9. Convert list of tuples to dictionary
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# dir = {}
# for i in pairs:
#     dir[i[0]] = i[1]
# print(dir)    

#Method - 2
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# print(dict(pairs))

# Q10. Sort list of tuples by second element
# data = [("a", 3), ("b", 1), ("c", 2)]
# print(sorted(data,key=lambda x: x[1]))

# Q.11 Sort numbers by their absolute value
# nums = [-5, 2, -3, 1, 4]
# print(sorted(nums,key=abs))

# Q.12 Sort string by length
# words = ["banana", "kiwi", "apple", "cherry"]
# print(sorted(words,key=len))

# # Q.13 Sort dictionary by values
# scores = {"Alice": 50, "Bob": 80, "Charlie": 70}
# result = sorted(scores.items(),key=lambda x: x[1]) 
# #.items() method returns a view object containing (key, value) pairs from a dictionary as tuples.
# print(result)
