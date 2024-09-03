import random

name = input("what is your name? ")
print("Good Luck !", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
turn = 12
print("Guess the characters : ")
guessed_word = "-" * len(word)
guessed_word = list(guessed_word)
print(' '.join(guessed_word))


def find_occurrences(string, char):
    positions = []
    index = string.find(char)
    while index != -1:
        positions.append(index)
        index = string.find(char, index + 1)
    return positions


while turn > 0 and guessed_word != list(word):
    guess = input("Guess a character : ")
    if guess in word:
        indexes = find_occurrences(word, guess)
        for position in indexes:
            guessed_word[position] = guess
        print(' '.join(guessed_word))
    else:
        print("wrong character")
        turn -= 1
        print("You have", turn, "more guesses")
          

if turn == 0:
    print("You lose")
else:
    print("you win")
