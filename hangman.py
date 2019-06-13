"""
Practice Python exercise 32
Hangman
http://www.practicepython.org/exercise/2017/01/10/32-hangman.html
"""

import random
inputWords = [ "aíre", "allow", "beautiful", "cars", "define", "exotic", "frank", "gnat"]


words = []

for x in inputWords:
  words.append(x.upper())


def pick_random_word():
  """
  This function picks a random word from the SOWPODS
  dictionary. 
  """
  # generate a random index
  # -1 because len(words) is not a valid index into the list `words`
  index = random.randint(0, len(words) - 1)

  # print out the word at that index
  word = words[index].strip()
  return word


def ask_user_for_next_letter():
  letter = input("Guess your letter: ")
  return letter.strip().upper()


def generate_word_string(word, letters_guessed):
  output = []
  for letter in word:
    if letter in letters_guessed:
      output.append(letter.upper())
    else:
      output.append("_")
  return " ".join(output)


if __name__ == '__main__':
  WORD = pick_random_word()

  letters_to_guess = set(WORD)
  correct_letters_guessed = set()
  incorrect_letters_guessed = set()
  num_guesses = 0

  print("Welcome to Hangman!")
  while (len(letters_to_guess) > 0) and num_guesses < 6:
    guess = ask_user_for_next_letter()
    # check if we already guessed that
    # letter
    if guess in correct_letters_guessed or \
        guess in incorrect_letters_guessed:
      # print out a message
      print("You already guessed " + guess)
      continue

    # if the guess was correct
    if guess in letters_to_guess:
      # update the letters_to_guess
      letters_to_guess.remove(guess)
      # update the correct letters guessed
      correct_letters_guessed.add(guess)
    else:
      incorrect_letters_guessed.add(guess)
      # only update the number of guesses
      # if you guess incorrectly
      num_guesses += 1

    word_string = generate_word_string(WORD, correct_letters_guessed)
    if num_guesses == 6: print(word_string, "\n    ____ \n   |    | \n   |    o\n   |   /|\ \n   |    |\n   |   /  \n   |\n  _|_ \n |   |______\n |__________|")
    if num_guesses == 5: print(word_string, "\n    ____ \n   |    | \n   |    o\n   |   /|\ \n   |    |\n   |     \n   |\n  _|_ \n |   |______\n |__________|")
    if num_guesses == 4: print(word_string, "\n    ____ \n   |    | \n   |    o\n   |   /|\ \n   |    \n   |     \n   |\n  _|_ \n |   |______\n |__________|")
    if num_guesses == 3: print(word_string, "\n    ____ \n   |    | \n   |    o\n   |   /| \n   |    \n   |    \n   |\n  _|_ \n |   |______\n |__________|")
    if num_guesses == 2: print(word_string, "\n    ____ \n   |    | \n   |    o\n   |    | \n   |\n   |\n   |\n  _|_ \n |   |______\n |__________|")
    if num_guesses == 1: print(word_string, "\n    ____ \n   |    | \n   |    o\n   |\n   |\n   |\n   |\n  _|_ \n |   |______\n |__________|")
    if num_guesses == 0: print(word_string, "\n    ____ \n   |    | \n   |    \n   |\n   |\n   |\n   |\n  _|_ \n |   |______\n |__________|")
        

    print("You have {} guesses left".format(6 - num_guesses))

  # tell the user they have won or lost
  if num_guesses < 6:
    print("Congratulations! You correctly guessed the word {}".format(WORD))
  else:
    print("Sorry, you lost! Your word was {}".format(WORD), "\n    ____ \n   |    | \n   |    o\n   |   /|\ \n   |    |\n   |   / \  \n   |\n  _|_ \n |   |______\n |__________|")