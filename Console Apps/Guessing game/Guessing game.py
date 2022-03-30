from random import choice

print("Country Guessing Game")
print(" Hi Welcome this game is made by Ai-sphinx and Clark!")
print(" Mechanics: Guess the country You have only 5 guesses each game")


def initialize_list():
    global words
    with open('countries.txt', 'r') as file:
        c = file.readlines()
        words = []
        for x in c:
            e = x.strip().lower()
            words.append(e)


initialize_list()
secret_word = choice(words).lower()
guess = None
guess_count = 0
guess_limit = 10
out_of_guesses = False

while True:

    if guess != secret_word and not (out_of_guesses):
        guess = input("Enter guess: ").lower()
        # print("The answer is", secret_word)
        guess_count += 1
        if guess_count == 3:
            firstletter = secret_word[0]
            print("It starts with letter", firstletter)
        elif guess_count == 6:
            secondletter = secret_word[1]
            print("The second letter is", secondletter)
            continue
        elif guess_count == 10:
            out_of_guesses = True
            print("Out of guesses, You Lose! Please try again.")
            print("The answer is", secret_word.capitalize())
            break
    else:
        print("You got the correct answer, You win!")
        break