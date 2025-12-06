friends = ["apple", "orange", 5, 343.3,  False, "mati", "banana" ]

print(friends)

friends.append("awais")

print(friends)

l1= [1,2,34,4,5,67,78,32]

# l1.sort()

# l1.reverse()

# l1.insert(4, 454)

value = (l1.pop(3))

print(value)

print(l1)

l1.remove(34)
print(l1)  # Output: [1, 2, 5, 67, 78, 32]


fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'orange']

fruits.extend(["grape", "kiwi"])
print(fruits)  # Output: ['apple', 'mango', 'banana', 'orange', 'grape', 'kiwi']

fruits.remove("banana")
print(fruits)  # Output: ['apple', 'mango', 'orange', 'grape', 'kiwi']

fruits.pop()        # removes 'kiwi'
fruits.pop(1)       # removes 'mango'
print(fruits)       # Output: ['apple', 'orange', 'grape']


fruits.clear()
print(fruits)  # Output: []


numbers = [10, 20, 30, 20]
print(numbers.index(20))  # Output: 1


print(numbers.count(20))  # Output: 2


numbers.sort()
print(numbers)  # Output: [10, 20, 20, 30]

numbers.sort(reverse=True)
print(numbers)  # Output: [30, 20, 20, 10]


numbers.reverse()
print(numbers)  # Output: [10, 20, 20, 30] (after reversing again)


new_list = numbers.copy()
print(new_list)  # Output: [10, 20, 20, 30]



