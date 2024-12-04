import random

the_number = random.randint(1, 55)
guess = int(input("Take a guess: "))
tries = 1

while guess != the_number:
    if guess > the_number:
     print("Lower...")
    else:
       print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")