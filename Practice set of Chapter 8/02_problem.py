f = int(input("Enter temperature in Fahrenheit: "))

def f_to_c(f):
    c = (f - 32) * 5 / 9
    return c


c = f_to_c(f)





print(f" {round(c, 2)}° C")