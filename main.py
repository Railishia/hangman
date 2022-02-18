import random

# figures for lives
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

word_list = ["aardvark", "baboon", "camel"]
# choosing random word from a word_list
chosen_word = random.choice(word_list)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#  assigning '_' for every letter in chosen word
display = list()
for i in chosen_word:
  display.append('_')

# looping through whole word until theres no '_'
while ('_' in display) and (lives >= 1):
  # taking users input with a letter
  guess = input("Guess a letter: ").lower()

  # checking if guessed letter is in the chosen word
  index = 0
  for letter in chosen_word:
      if letter == guess:
          # print("Right")
          display[index] = letter
          index += 1
      else:
          # print("Wrong")
          index += 1

  print(display)

# handling number of lives and hagman figure printing
  if (guess in chosen_word):
    print("Right")
    print(stages[lives])
  else:
    print("Wrong")
    lives -= 1
    print(stages[lives])

# checking if the user won
if lives < 1:
  print('You lose.')
  print('The word was: ' + chosen_word)
else:
  print('You win.')
  print('The word is: ' + chosen_word)
