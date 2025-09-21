## If elese condition practice are already used so not repeat here.
## lets check for loop
# for num in [1,2,5,6]:
#     print(num)

# for chr in "Hi":
#     print(chr)

# for i in range(10):
#     print(i)

# for i in range(2,10,2): #range(start,end,step)
#     print(i)

# Break and Continue you aready know. lets check "pass" in for loop.
# for i in range(10):
#     if i == 3:
#         pass # Implementation will be future. sometime it is not decided yet.
#     print(i)
### Real use case of pass ###
# When designing structure first and planning to fill logic later.
# def process_data():
#     pass  # TODO: implement later

# class DataHandler:
#     pass  # class will be defined later

# ✅ Lets your code run without errors while you’re still building it.
###########

### else with Loops
# for i in range(3):
#     print(i)
# else:
#     print("Loop completed")

### loop inside loop
# for i in range(3):
#     for j in ["Hi", "heelo", "sandip"]:
#         print(i,j)

### Looping with enumerate() and zip()
# for l_index, l_val in enumerate(["Hi","Sandip","How","Are","You"]):
#     print(l_index, l_val)

### zip will assign one array as key and other array as value. 
### if the number of elements are different then it will iterate upto minimum array element.

# nums = [1,2,3,4,5,6]
# names= ["sandip","rakesh","mohan","karan"]
# for i,j in zip(nums,names):
#     print(i,j)

## Q. Check if the number is prime or not
# def check_prime(s_number: int):    
#     is_prime = True
#     for i in range(2, s_number):
#         if(s_number % i == 0):
#             is_prime = False
#     return is_prime
# num = 1
# print(f"Number {num} " + ("Is prime" if check_prime(num) == True else "Is Not prime"))
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.
## Q.