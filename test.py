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


#range(start, stop, step)

# x = 1
# z = 7
# for b in range(x, z+1, 1):
#print(b)

# start_value = a_list[0]
# stop_value = a_list[-1]




