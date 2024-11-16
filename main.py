import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']



word_list = ["aardvark", "baboon", "camel", "raven", "whale", "sloth", "llama", "renegade", "anchorage", "cilantro"]

lives = 6

choose_word=random.choice(word_list)
print(choose_word)

placeholder = ""
word_length =len(choose_word)

for _ in range(word_length):
    placeholder += "_"
print(placeholder)

game_over =False
correct_letters =[]

while not game_over:
    guess = input("Guess a letter: ").lower()

    display =""

    for letter in choose_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display+="_"

    print(display)

    if guess not in choose_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over=True
        print("You win!")

    print(stages[lives])


