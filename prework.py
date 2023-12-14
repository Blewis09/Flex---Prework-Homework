# def hello_name(user_name):
user_name = input("What is your name? ")
print("Hello " + user_name)

# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
# def first_odds():
for x in range (1,100,2):
    print(x)
       
   
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
# def max_num_in_list(a_list):
list=[]
print(max(list))
    
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
# def is_leap_year(a_year):
if a_year % 400 == 0:
    return True 
if a_year % 100 == 0:
    return False 
if a_year % 4 == 0:
    return True 
else:
    return False 

