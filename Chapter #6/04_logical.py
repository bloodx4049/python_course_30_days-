a = 10
print(a > 5 and a < 20)    # True
print(a > 5 and a > 20)    # False

a = 10
print(a > 5 or a < 5)      # True
print(a < 5 or a < 1)      # False

is_sunny = True
print(not is_sunny)   # False

age = 18
citizen = True

if age >= 18 and citizen:
    print("You can vote!")
else:
    print("You cannot vote.")

# and → Both must be true

# or → One true is enough

# not → Opposite

