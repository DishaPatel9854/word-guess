import random

name = input("What's your name: ")
print("Best of Luck!!", name)

words = ['pink', 'light', 'read', 'celery', 'cake', 'game']

print("Guess the word from the following: ")
print(words)

word = random.choice(words)
guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou Win")
        print("The word is:", word)
        break

    print()
    guess = input("Guess a character: ").lower()

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, 'more guesses')

    if turns == 0:
        print("You Loose")

      