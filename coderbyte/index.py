# Q.1 Reverse a given string without using slicing.
# s = "Hi I am sandip and I am programmer"
# m = len(s) - 1
# arr = []
# while(m >= 0):
#     arr.append(s[m])
#     m -= 1
# print("".join(arr))

# Q.2 Check if a string is a palindrome.
# s = "MalaM"
# if(s == s[::-1]):
#     print("Yes it is palindrome")
# else:
#     print("No it is not palindrome")

# Q.3 Determine if two strings are anagrams of each other.    
# Anagrams are two words or strings that have:
# The same characters
# With the same frequency
# But possibly in a different order
# ✅ Example
# "listen" and "silent" → anagrams
# "race" and "care" → anagrams

# def are_anagrams(s1, s2):
#     s1_arr = sorted(list(s1.replace(" ", "")))
#     s2_arr = sorted(list(s2.replace(" ", "")))
#     return s1_arr == s2_arr
# print(are_anagrams("listen", "silent"))  # True
# print(are_anagrams("care", "race"))  # True
# print(are_anagrams("care", "racce"))  # False

# Q.4 Find the first non-repeating character in a string.
# def first_non_repeating(s):
#     non_repeat = ""
#     for chr in s:
#         if(s.count(chr) == 1):
#             non_repeat = chr
#             break
#     return non_repeat
# print(first_non_repeating("aabbdceeff"))

# Q.5 Count word frequencies in a sentence.

# def find_freq(s):
#     arr = s.lower().split(" ")
#     freq = {}
#     for a in arr:
#         if(a in freq):            
#             freq[a] += 1
#         else:
#             freq[a] = 1
#     return freq
# print(find_freq("My name is sandip Name is good Good is ok"))

# Method - 2
# from collections import Counter
# def find_freq(s):
#     return dict(Counter(s.lower().split(" ")))
# print(find_freq("My name is sandip Name is good Good is ok"))

## Q.6 Remove duplicates from a list while maintaining order.
# m_list = [2,3,2,5,7,8,5,9]
# def remove_duplicate(l):
#     temp = []
#     for item in l:
#         if item not in temp:
#             temp += [item]        
#     return temp
# print(remove_duplicate(m_list))

## Q.7 Check if any two numbers in a list sum to a target value.
# m_list = [2, 23, 32, 53, 67, 42, 9]
# def check_two_number_sum(n_list, target):    
#     pair_list = []
#     for i,num in enumerate(n_list):
#         for j,next_num in enumerate(n_list[i+1:]):
#             if((num + next_num) == target):                
#                 pair_list += [(num, next_num)]        
#     return pair_list
# print(check_two_number_sum(m_list, 51))

#Method: 2
# m_list = [2, 23, 32, 53, 67, 42, 9]
# def check_two_number_sum(n_list, target):
#     seen = set()
#     pairs = []
#     for num in n_list:
#         needed = target - num
#         if needed in seen:
#             pairs += [(needed, num)]
#         seen.add(num)
#     return pairs
# print(check_two_number_sum(m_list, 51))    

## Q.8 Merge two sorted lists into one sorted list.
# m1 = [5,8,10,12]
# m2= [2,5,6,8,9,11]
# def merge_list(m1, m2):
#     return sorted(m1 + m2)
# print(merge_list(m1, m2))

## Q.9 Implement binary search on a sorted list.
# n_list = [2, 5, 9, 12, 23]
# def binary_search(n_list, target, start_point, end_point):   
#     if((end_point - start_point) == 1):
#         if(n_list[start_point] == target):
#             return start_point
#         elif((end_point < len(n_list)) and (n_list[end_point] == target)):
#             return end_point
#         else:
#             return "Not Found"        
#     middle_point = ((start_point + end_point) // 2)
#     if(n_list[middle_point] == target):
#         return middle_point
#     elif(n_list[middle_point] > target):
#         return binary_search(n_list, target, start_point, middle_point)
#     else:
#         return binary_search(n_list, target, middle_point, end_point)
# print(binary_search(n_list, 99, 0, len(n_list)))

#Method - 2
# n_list = [2, 5, 9, 12, 23, 27, 36, 39, 45, 51, 59, 65, 68, 73, 81, 92, 98, 100]
# def binary_search(n_list, target, start_point, end_point):
#     # 🔹 if start > end → target not found
#     if start_point > end_point:
#         return "Not Found"
#     # 🔹 middle index
#     middle_point = (start_point + end_point) // 2
#     if n_list[middle_point] == target:
#         return middle_point
#     elif n_list[middle_point] > target:
#         return binary_search(n_list, target, start_point, middle_point - 1)
#     else:
#         return binary_search(n_list, target, middle_point + 1, end_point)
# # ⚡ pass len(n_list)-1 as end_point (last valid index)
# print(binary_search(n_list, 101, 0, len(n_list)-1))



## Q.10 Generate the first n Fibonacci numbers.
# def generate_fab(n):
#     i = 0
#     arr = []
#     while(i < n):
#         if(i < 2):
#             arr += [1]
#         else:
#             arr += [(arr[i-1] + arr[i-2])]
#         i += 1
#     return arr
# print(generate_fab(8))

## Q.11 Check if a number is prime.
# def check_prime(n):   
#     if n < 2:
#         return "Non Prime"
#     if n == 2:
#         return "Prime" 
#     i = 2
#     half = (n // 2) + 1
#     is_prime = "Prime"    
#     while(i <= half):
#         if((n % i) == 0):
#             is_prime = "Non Prime"
#             break
#         i += 1
#     return is_prime
# print(check_prime(3))

## Q.12 Find the missing number in a consecutive sequence.
# def find_missing(p_list):    
#     missing = (set(range(p_list[0], (p_list[-1] + 1)))) - set(p_list)
#     if(len(list(missing)) > 0):
#         return list(missing)[0]
#     return ""    
# n_list = [4, 5, 6, 7,8,9, 10]
# print(find_missing(n_list))

## Q.13 Check if brackets in a string are balanced.
# def check_balance_brackets(i_string):
#     to_array = list(i_string)
#     num_breckets = 0    
#     for chr in to_array:
#         if(chr == '('):
#             num_breckets += 1
#         elif(chr == ')'):
#             num_breckets -= 1
#         if(num_breckets < 0):            
#             break
#     return True if (num_breckets == 0) else False
# print(check_balance_brackets("my ()(balan(c(e) ( string )())"))

## Q.14 Find the maximum sum subarray (Kadane’s algorithm).
# def kandane_subarray(i_list):
#     max_number = i_list[0]
#     result = (max_number, [i_list[0]])
#     for i,val in enumerate(i_list):
#         if(val > max_number):
#             max_number = val   
#             result = (max_number, [val])
#         current_sum = 0        
#         for m,sub_val in enumerate(i_list[i:]):
#             current_sum += sub_val
#             if(current_sum > max_number):
#                 max_number = current_sum
#                 result = (max_number, i_list[i:(i+m)+1])
#     return result
# my_list = [ -2, 1, -3, 4, -1, 2, 1, -5,90 ]
# print(kandane_subarray(my_list))

###Method:2

# def kandane_subarray(i_list):
#     greater_sum = i_list[0]  
#     current_sum = 0   
#     greater_start = greater_end = 0

#     for l_index, l_num in enumerate(i_list):
#         if (l_num > current_sum):
#             if (current_sum > 0):
#                 current_sum += l_num
#             else:
#                 current_sum = l_num
#                 greater_start = greater_end = l_index
#         else:
#             current_sum = current_sum + l_num
#         if(current_sum > greater_sum):
#             greater_sum = current_sum
#             greater_end = l_index
            
#     return (greater_sum,(greater_start, greater_end))
# my_list = [4, 3, -2, 100, -1]
# print(kandane_subarray(my_list))

## Q.15 Find the length of the longest substring without repeating characters.
def longest_unique_substring(input_str):
    max_list = current_list = []     
    for i,chr in enumerate(input_str):
        if(chr in current_list):
            current_list = current_list[current_list.index(chr) + 1 :]
        current_list += [chr]    
        if(len(current_list) > len(max_list)):
            max_list = current_list                
    return "".join(max_list) if len(max_list) > 0 else ""
print(longest_unique_substring("xyzxyztuv"))

## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.