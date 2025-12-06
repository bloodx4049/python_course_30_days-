#set this collection of well define Objects

my_set = {1, 2, 3, 4, 5}

print(my_set)  # {1, 2, 3, 4, 5}    

print(type(my_set))  # <class 'set'>

print(len(my_set))  # 5 

# set does not allow duplicate values


my_set = {1, 2, 2, 3, 4, 4, 5}

print(my_set)  # {1, 2, 3, 4, 5}  

# set can have different data types

my_set = {1, 2.5, "Hello", True, (1, 2)}

print(my_set)  # {1, 2.5, 'Hello', True, (1, 2)} 

# set does not support indexing


# print(my_set[0])  # TypeError: 'set' object is not subscriptable

e = set() # empty set
print(e)  # set()
e = set([1, 2, 3])  # creating a set from a list
print(e)  # {1, 2, 3}   
