## Q.1 Sorting Complex Data
##you are given a list of tuples (name, score). Sort by score (second item).
# students = [("Vikas", 80), ("Zmit", 95), ("Ravi", 70)]
# print(sorted(students, key=lambda x: x[1]))

## Q.2 From a list of numbers, filter only even numbers.
# nums = [1, 2, 3, 4, 5, 6]
# print(list(filter(lambda x: x % 2 ==0, nums)))

## Q.3 Convert list of strings to their lengths.
# words = ["apple", "banana", "cherry"]
# print(list(map(lambda x: len(x), words)))

## Q.4 Calculate the product of all numbers using reduce.
# nums = [2, 3, 4]
# from functools import reduce
# print(reduce(lambda a,b: a * b, nums))

## Q.5 Custom Sort on String Length
#sort word by their length
# words = ["apple", "kiwi", "banana"]
# print(sorted(words, key=lambda x: len(x)))

