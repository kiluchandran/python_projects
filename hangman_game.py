import random

words = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
words = words.split()
word = random.choice(words)

if __name__ == "__main__":
    print("Guess the word!HINT:word is a name of a fruit ")

    for i in word:
        print("_", end=" ")

    print()

    turn = len(word) + 2
    guesses = ""
    try:
        while turn > 0:
            guess = input("Guess a letter:")

            if not guess.isalpha():
                print("Guess a letter")
                continue
            elif len(guess) > 1:
                print("Guess only a single letter")
                continue

            guesses += guess
            failed = 0

            for char in word:
                if char in guesses:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
                    failed += 1
            print()

            if failed == 0:
                print("You win")
                print("The word is: ", word)
                break

            if guess not in word:
                print("Wrong letter")
                turn -= 1
                print("you have", turn, "more guesses")
                if turn == 0:
                    print("You loose")


    except KeyboardInterrupt:
        print()
        print("Try again")
        exit()

