# s1 = 'hello'
# s2 = "Python"
# s3 = '''
# This
# is
# multiline
# string
# '''
# print(s1,s2,s3)

## Strings are Immutable so You cannot change a character inside a string.
# name = "Apple"
# name[0] = "a"   #Error: 'str' object does not support item assignment
# print(name)

##Instead, you create a new string:
# name = "Apple"
# new_name = "a" + name[1:]
# print(new_name)

## Slicing
## string[start : end : step]
## start → index where slice begins (inclusive).
## end → index where slice ends (exclusive).
## step → interval (default = 1)
# word = "Hello Python"
# print(word[0:4])     # index 0 to 3
# print(word[:4])      # start defaults to 0
# print(word[2:])      # till the end
# print(word[:])       # full copy
# print(word[1:7:2])   # (index 1 to 7 with step 2)
# print(word[-3])      # last 3rd index
# print(word[::-1])    # reverse the string