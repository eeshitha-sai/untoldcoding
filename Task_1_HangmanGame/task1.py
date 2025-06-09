import random

words = ["apple", "banana", "grape", "orange", "peach"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
display_word = ["_"] * len(secret_word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {max_guesses} incorrect guesses allowed.")

while incorrect_guesses < max_guesses and "_" in display_word:
    print("\nCurrent word:", " ".join(display_word))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nSorry! You ran out of guesses. The word was:", secret_word)
