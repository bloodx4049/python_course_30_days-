                                 # Arithmetic Operators
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulus (remainder)
print(a ** b)  # Power (10^3 = 1000)
print(a // b)  # Floor division

                                            # 2. Assignment Operators
a = 10
a += 2   # x = x + 2
a -= 1   # x = x - 1
a *= 3   # x = x * 3
a /= 2   # x = x / 2
a %= 3   # x = x % 3
a //= 2  # x = x // 2
a **= 2  # x = x ** 2

print(a)

                                            # 3. Comparison Operators
a = 5
b = 3

print(a == b)   # Equal?
print(a != b)   # Not equal?
print(a > b)    # Greater?
print(a < b)    # Less?
print(a >= b)   # Greater or equal?
print(a <= b)   # Less or equal?

                                        # 4. Logical Operators

x = True
y = False

print(x and y)   # Both true?
print(x or y)    # At least one true?
print(not x)     # Reverse x
                                       
                                    #    5. Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)        # True (same object)
print(a is c)        # False (same values, different object)

print(a is not c)    # True

                                    #  6. Membership Operators

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)        # True
print("orange" not in fruits)   # True


                                #   7. Bitwise Operators

a = 5    # 0101
b = 3    # 0011

print(a & b)   # AND → 0001 = 1
print(a | b)   # OR  → 0111 = 7
print(a ^ b)   # XOR → 0110 = 6
print(~a)      # NOT → -(a+1) = -6
print(a << 1)  # Left shift → 1010 = 10
print(a >> 1)  # Right shift → 0010 = 2

