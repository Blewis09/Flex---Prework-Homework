# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("Hello " + "_" + user_name.upper() + "!")

hello_name("Bethany")


# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for x in range (1,100,2):
        print(x)

first_odds()

   
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    return(max(a_list))
my_list=[2,4,55,55,100]   
max_num_in_list(my_list)
    
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True 
    if a_year % 100 == 0:
        return False 
    if a_year % 4 == 0:
        return True 
    else:
        return False 

print(is_leap_year(2066))

#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    consecutive_list = []
    for n in range(a_list[0],a_list[-1]+1, 1):
       consecutive_list.append(n) 
    if a_list == consecutive_list:
        print(True) 
    else:
        print(False)

test_list = [101,102,103,104,105,106,107,108,109,110]
is_consecutive(test_list)
