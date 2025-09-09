# text = "hello python"
# print(text.capitalize())
# print(text.upper())
# print(text.lower())
# print(text.title())

## stripe
# text = "   hello python   "
# print(text.strip())
# print(text.rstrip())
# print(text.lstrip())

# sentence = "Python is amazing and Python is powerful"
# print(sentence.find("Python"))  #first index. if not found return -1 to calling function.
# print(sentence.rfind("Python"))  #last index
# print(sentence.index("Python"))  #first index. but if not found it return error to calling function
# print(sentence.index("Python"))  #first index. but if not found it return error to calling function
# print(sentence.count("Python"))  #count of substring occurence

# text = "I love Java"
# new_text = text.replace("Java", "Python")
# print(new_text) #make sure it not replace in original string.

####Split & Join
# line="apple,banana,cherry"
# fruits = line.split(',')
# print(fruits)
# # Join back with separator
# joined = "-".join(fruits)
# print(joined)

# fname = 'sandip'
# lname = 'bhalodiya'
# print(fname + ' ' + lname)
# print(fname * 3) #sandipsandipsandip

# text="Python is used widely for data operation in AI/ML"
# print("Python" in text)
# print("Java" in text)
# print("hdfc" not in text)
# print(len(text))

# fname = 'sandip'
# lname = 'bhalodiya'
# age = 40
# print("My name is %s and I am %d year old" % (fname, age))

# fname = 'sandip'
# lname = 'bhalodiya'
# age = 40

# print("My name is {} and I am {} year old" . format(fname, age))
# print("My name is {0} and I am {1} year old".format(fname, age))
# print("My name is {n} and I am {a} year old".format(n=fname, a=age))

# The most modern and recommended way.
# print(f"I am {fname} and I am {age} years old")

# pi = 3.14159265
# print("Value of pi: %.2f" % pi) # up to 2 decimal
# print("value of pi {:.3f}".format(pi)) # up to 3 decimal
# print(f"value of pi:{pi:.3f}") # up to 3 decimal

### Escaping
# print("Hello\nworld")
# print("Hello\tWorld")
# print("C:\\Users\\Sandip")
# print("It\'s Good catch")
# print("He said \"Python is a fun\"")

###Iteration
# text = "I am python. I used very much in AI/ML"
# for chr in text:
#     print(chr)

# for i,chr in enumerate(text):
#     print(i, chr)

# text = "I am python. I used very much in AI/ML"
# wovel = "aeiouAEIOU"
# count = 0
# for chr in text:
#     if chr in wovel:
#         count+=1
# print("Number of wovels: ",count)

# s1 = "python"
# s2 = "Python"
# s3 = "python"
# print(s1 == s2) #case sensitive
# print(s1 == s3)
# print(s1 != s2)

# Relational Operators (<, >, <=, >=)
# Strings are compared lexicographically (like dictionary order), based on Unicode values.
# print("apple" < "banana")
# print("abc" < "abd")
# print("Zebra" < "apple")

# You can check Unicode value using ord():
# print(ord("Z"))
# print(ord("a"))

# s1="python"
# s2="Python"
# print(s1.lower() == s2.lower())

# words = ["Banana", "apple", "Cherry"]

# print(sorted(words))
# print(sorted(words, key=str.lower)) #consider str is python built in class.

# # Advanced string methods.
# text = "Python programming"
# print(text.startswith("Py"))
# print(text.endswith("ing"))

# s="Python3"
# print(s.isalpha()) #check only alpthabetical(letters)
# print(s.isalnum()) # check letters + numbers -- true
# print("12345".isdigit()) #check digit
# print("12.5".isdigit()) #False . not allowed

# print("hello".islower()) # check only lower case
# print("Hello".istitle()) # check for title case
# print("HELLO".isupper()) #check for upper


# Useful for formatting output.
word = "Python"

print(word.center(10, "-"))  # '--Python--'  # create 10 character length string
print(word.ljust(10, "*"))   # 'Python****'
print(word.rjust(10, "."))   # '....Python'
print(word.center(5,"-"))    # 'Python' cannot cover within 10 chars length so no formatting.

# zfill() → Zero Padding
# mynum="42"
# print(mynum.zfill(5))  #00042 fill with zero to achive 5 length