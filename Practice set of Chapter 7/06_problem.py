#5! = 1*2*3*4*5 = 120
n = int(input("Enter a number: "))
factorial = 1
for i in range(1,n+1):
    factorial = factorial*i
    print(f"the factorial of {n} is {factorial}")