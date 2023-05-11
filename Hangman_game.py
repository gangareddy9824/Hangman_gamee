import random

# Define a list of words to choose from
words = ['apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig']

# Select a random word from the list
word = random.choice(words)

# Define a list of dashes to represent the unguessed letters in the word
dashes = ['_'] * len(word)

# Loop until the user guesses the word or runs out of guesses
guesses_left = 6
while True:
    # Print the current state of the game
    print(' '.join(dashes))
    print('Guesses left:', guesses_left)

    # Ask the user to guess a letter
    guess = input('Guess a letter: ')

    # Check if the letter is in the word
    if guess in word:
        # Replace the appropriate dashes with the letter
        for i in range(len(word)):
            if word[i] == guess:
                dashes[i] = guess
    else:
        # Decrement the number of guesses left
        guesses_left -= 1

    # Check if the user has won or lost
    if '_' not in dashes:
        print('Congratulations! You guessed the word.')
        break
    elif guesses_left == 0:
        print('Sorry, you ran out of guesses. The word was', word)
        break
