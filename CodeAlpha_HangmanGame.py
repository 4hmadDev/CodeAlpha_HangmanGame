import random

words = ["ahmad","pen","book","laptop","phone"]
word = random.choice(words)

gussed_word = []
wrong_word = 0

print("Welcome to hangman game")
print("you have 6 attempts")

while wrong_word < 6:

  display = ""
  for letter in word:
    if letter in gussed_word:
      display += letter
    else:
        display += "_"
    print("Word: ",display)

  if "_" not in display:
    print("You won")
    break

  guess = input ("Guess a letter: ")
  if guess in gussed_word:
    print("You already guessed this letter")
  elif guess in word:
    gussed_word.append(guess)
    print("Correct guess")
  else:
    wrong_word += 1
    print("Wrong guess")
  if wrong_word == 6:
    print("You lost the word was",word)