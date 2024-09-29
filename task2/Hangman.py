import random
word = "SHADOWFOX"
hints = ["_"] * len(word)
guesses = 6
progress_bar = ["_"] * len(word)

while guesses > 0:
    print(" ".join(hints))
    print(" ".join(progress_bar))
    guess = input("Guess a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hints[i] = guess
                progress_bar[i] = "*"
    else:
        guesses -= 1
        print("Incorrect guess. Remaining guesses:", guesses)
    if "_" not in hints:
        print("Congratulations! You won!")
        break
else:
    print("Game over. The word was", word)