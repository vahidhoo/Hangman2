from random import choice


def game():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = choice(words)
    letters = set(word)
    guessed_letters = set()
    word_display = ['-' for letter in word]

    print('H A N G M A N\n')
    guesses = 8  # lives
    while guesses:
        print(''.join(word_display))
        guess = input('Input a letter: ')

        if len(guess) > 1 or len(guess) == 0:
            print('You should input a single letter')
            print()
            continue

        if not guess.islower():
            print('Please enter a lowercase English letter')
            print()
            continue

        if guess not in letters and guess not in guessed_letters:
            guesses -= 1
            print("That letter doesn't appear in the word")
            guessed_letters.update(guess)

        elif guess in guessed_letters:
            if guess in word and guess not in guessed_letters:
                guesses -= 1
            print("You've already guessed this letter")
        else:
            guessed_letters.update(guess)
            for i in range(len(word_display)):
                if guess == word[i]:
                    word_display[i] = guess

        if word_display.count('-') < 1:
            print('You guessed the word!')
            print('You survived!')
            break
        if guesses == 0:
            print('You lost!')
            break
        else:
            print()


def main():
    while True:
        menu = input('Type "play" to play the game, "exit" to quit:')

        if menu == 'play':
            game()
        elif menu == 'exit':
            break


main()
