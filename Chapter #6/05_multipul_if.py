a = int(input("Enter your age: "))

# Using if-elif-else ladder to check age categories

# IF statement number 1

if(a%2==0):
    print("Your age is an even number.")
#end of IF statement 1

# IF statement number 2


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

    #end of IF statement 2


print("Thank you for using the age checker.")

#if is work without else and elif also and
# all if statements are independent to each other
# else and elif are always dependent to if statement

