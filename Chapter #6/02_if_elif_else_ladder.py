a = int(input("Enter your age: "))

# Using if-elif-else ladder to check age categories
if (a >= 18):
    print("You are an adult.")

    print("You can vote.")

elif(a<0):
    print("Invalid age entered.")

elif(a==0):
    print("Age cannot be zero.")
    print("Please enter a valid age.")
    
else:
    print("You are a minor.") 

    print("You cannot vote.")

print("Thank you for using the age checker.")
