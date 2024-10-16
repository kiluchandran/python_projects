import random


num = random.randrange(1000,10000)
print(num)
n = int(input("Guess the 4 digit number:"))
if n == num:
    print("Great!You guessed the number in just 1 try!You are a Mastermind!")
else:
    guess = 0
    while n != num:
        guess += 1
        num1 = str(num)
        n1 = str(n)
        correct = ["X"] * 4
        count = 0
        for i in range(0,4):
            if n1[i] == num1[i]:
                correct[i] = n1[i]
                count += 1
        if count != 0:
            print("Not quite the number.But you did get",count,"digit correct!")
            print("Also these numbers in your input were correct")
            for k in correct:
                print(k, end="")
            print("\n")
            n = int(input("Enter your next choice of numbers:"))
        elif count == 0:
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers:"))

    if n == num:
        guess += 1
        print("You have become a Mastermind.")
        print("it took you only ",guess,"tries")


