## Q.1 Count word frequency
# def count_words(s_input):
#     word_meta = {}
#     for s in s_input.split(" "):
#         word_meta[s] = (word_meta[s] + 1) if word_meta.get(s) else 1
#     return word_meta

# print(count_words("apple banana apple orange banana apple"))

#Method 2
# from collections import Counter
# def count_words(s_input):
#     return dict(Counter(s_input.split(" ")))

# print(count_words("apple banana apple orange banana apple"))

## Q.2 Find key with max value
# def find_max_value_key(d_input):
#     return max(d_input,key=d_input.get)
# print(find_max_value_key({'a': 3, 'b': 7, 'c': 5}))

## Q.3 Reverse a dictionary (swap keys and values)
# def reverse_dictionary(d_input: dict) -> dict:
#     return {value:key for key, value in d_input.items()}
# print(reverse_dictionary({'a': 1, 'b': 2, 'c': 3}))

## Q.4 Merge two dictionaries
# def merge_dictionaries(d1: dict, d2: dict) -> dict:    
#     #Method - 1
#     return {**d1, **d2}
#     #Method - 2
#     # d1.update(d2)
#     # return d1
# d1 = {'a': 1, 'b': 2} 
# d2 = {'b': 3, 'c': 4}
# print(merge_dictionaries(d1, d2))

## Q.5 Find unique elements in list
# l1 = [1,2,2,3,4,4,5]
# print(set(l1))

## Q.6 Find common elements of two lists
# l1 = [1,2,3,4]
# l2 = [3,4,5,6]
# print(set(l1) & set(l2))

## Q.7 Find elements only in first list
# l1 = [1,2,3,4]
# l2 = [3,4,5,6]
# print(set(l1) - set(l2))

## Q.8 Remove duplicates but keep order
# def remove_duplicate(l_input):
#     seen = []
#     for e in l_input:
#         if e not in seen:
#             seen.append(e)
#     return seen
# l1 = ['a','b','a','c','b']
# print(remove_duplicate(l1))


## Q.9 Group words by their set of letters
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
