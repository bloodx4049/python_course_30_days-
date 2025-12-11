a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))

if (b == 0):
    raise ZeroDivisionError("hey our program is not meant to division number by zero")
else:
    print(f"the division a/b is {a/b}")