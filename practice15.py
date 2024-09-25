#Write a Python program to remove a key from a dictionary

my_dict = {1:23,2:34,3:61,4:32,5:30}

print(my_dict)

if 3 in my_dict:
    del my_dict[3]

print(my_dict)   