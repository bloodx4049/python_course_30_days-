import random
n = random.randint(1,100)
a = -1
guesses = 1
while(a !=n):
    
    a = int(input("Guess a Number: " ))

    if (a>n):
         print("Lower Number Please")
         guesses += 1
    elif(a<n):
         print("Higher the Number:")
    guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempt")