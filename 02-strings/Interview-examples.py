# 1. Reverse a String
# s="Python"
# print(s[::-1])
# print("".join(reversed(s)))

# 2.check palingdrome
# s='madam'
# if(s.lower() == s[::-1].lower()):
#     print("it is palingdrome")
# else:
#     print("Not Palingdrome")

# 3. Count Vowels
# s="I am sandip and I am programmer"
# vowels = 'aeiouAEIOU'
# cnt = 0
# for chr in s:
#     if chr in vowels:
#         cnt += 1
# print(cnt)

# 4. Remove duplicate
# s="I am sandip and I am programmer"
# arr = []
# for chr in s:
#     if chr not in arr:
#         arr.append(chr)
# print("".join(arr))

# 5.First Non-Repeated Character
# s = "aabbcdeff"
# r = ""
# for i,chr in enumerate(s):        
#     if((i != 0) and (chr not in s[i+1:len(s)]) and (chr not in s[0:i])):        
#         r=chr
#         break
# print(r)        

# s = "aabbcdeff"
# for chr in s:
#     if(s.count(chr) == 1):
#         print("First occurence: " + chr)
#         break

# 6. Most Frequent Character
# s = "aabbcdeffb"
# r_char = ""
# r_count = 0
# for chr in s:
#     if(s.count(chr) > r_count):
#         r_char = chr
# print(r_char)

## Method - 2
# s = "aabbcdeffbf"
# r_dir = {}
# for chr in s:
#     r_dir[chr] = s.count(chr)
# print(max(r_dir, key=r_dir.get))    