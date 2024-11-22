import random

from random import randint
# i used the randint function to generate a random number between 1 and 10 
# i am stuggling to code please help!
name = input("what is your name?: ")
# i am asking for your name so put it in the terminal
print(f"you are a failure, {name}")

print(f"thank you for playing, {name}")

random_number = random.randint(1, 11)
number = input("choose a number between 1 & 10: ")
if number == random_number:
    print("you win yay!!")
else:
    print("try again!")