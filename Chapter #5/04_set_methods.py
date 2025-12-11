# set methods

my_set = {1, 2, 3}

print(my_set)  # {1, 2, 3}  

my_set.add(4)

print(my_set)  # {1, 2, 3, 4}

my_set.add(2)  # adding duplicate value

print(my_set)  # {1, 2, 3, 4}   

my_set.update([5, 6, 7])

print(my_set)  # {1, 2, 3, 4, 5, 6, 7}  

my_set.update({8, 9})
print(my_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}  
my_set.discard(3)
print(my_set)  # {1, 2, 4, 5, 6, 7, 8, 9}  
my_set.discard(10)  # discarding non-existing value
print(my_set)  # {1, 2, 4, 5, 6, 7, 8, 9}           
my_set.remove(4)
print(my_set)  # {1, 2, 5, 6, 7, 8, 9}  
# my_set.remove(10)  # KeyError: 10
popped_value = my_set.pop()
print(popped_value)  # 1 (or any other element, as sets are unordered)
print(my_set)  # Remaining elements after pop
my_set.clear()
print(my_set)  # set()  
my_set = {1, 2, 3}
copy_set = my_set.copy()
print(copy_set)  # {1, 2, 3}    
frozen_set = frozenset([1, 2, 3])
print(frozen_set)  # frozenset({1, 2, 3})
# frozen_set.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'
print(frozen_set.union({4, 5}))  # frozenset({1, 2, 3, 4, 5})
print(frozen_set.intersection({2, 3, 4}))  # frozenset({2, 3})
print(frozen_set.difference({2, 3, 4}))  # frozenset({1})
print(frozen_set.isdisjoint({4, 5}))  # True
print(frozen_set.issubset({1, 2, 3, 4}))  # True
print(frozen_set.issuperset({1, 2}))  # True
print(frozen_set.symmetric_difference({3, 4, 5}))  # frozenset({1, 2, 4, 5})
# End of 04_set_methods.py

s = {1, 2, 3, 4, 5, "awais","mati"}

print(s, type(s))  # {1, 2, 3, 4, 5}
s.add(6)
print(s)  # {1, 2, 3, 4, 5, 6}
s.update([7, 8])
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8}
s.discard(2)
print(s)  # {1, 3, 4, 5, 6, 7, 8}
s.remove(3)
print(s)  # {1, 4, 5, 6, 7, 8}
popped_value = s.pop()
print(popped_value)  # 1 (or any other element, as sets are unordered)
print(s)  # Remaining elements after pop
s.clear()
print(s)  # set()