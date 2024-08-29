import math
import random



lower_bound=int(input("Enter lower bound:-"))
upper_bound=int(input("Enter upper bound:-"))

random_number = random.randint(lower_bound,upper_bound)
no_of_guesses=math.ceil(math.log(upper_bound-lower_bound+1,2))
print("You have only",no_of_guesses,"chances to guess the integer!")


guess_count=0
flag=False
while guess_count < no_of_guesses:
    guess_count+=1
    guess_number=int(input("Guess a number:-"))
    if guess_number == random_number:
        print("Congragulations you did it in ",guess_count,"try")
        flag=True
        break
    elif guess_number > random_number:
        print("You guessed too large")
    elif guess_count < random_number:
        print("You guesses too small")

if not flag:
    print("Better Luck Next Time")

