def inch_to_cm(inch):
    cm = inch * 2.54
    return cm

n = int(input("Enter length in inches: "))

cm = inch_to_cm(n)

print(f"{n} inches is equal to {cm} cm")