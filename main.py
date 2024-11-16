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

word_length =len(choose_word)

placeholder = "_" * len(choose_word)
print(placeholder)

game_over =False
correct_letters =[]

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed the letter {guess}")
        continue

    if guess not in choose_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You lose! The word was '{choose_word}'")
    else:
        correct_letters.append(guess)

    display =''.join([letter if letter in correct_letters else '_' for letter in choose_word])
    print(f"Current word: {display}")

    if '_' not in display:
        game_over = True
        print(f"You win! The word was '{choose_word}'.")
    
    print(stages[lives])

    # display =""

    # for letter in choose_word:
    #     if letter == guess:
    #         display += letter
    #         correct_letters.append(guess)
    #     elif letter in correct_letters:
    #         display += letter
    #     else:
    #         display+="_"

    # print(display)

    # if guess not in choose_word:
    #     lives -= 1
    #     if lives == 0:
    #         game_over = True
    #         print("You lose.")

    # if "_" not in display:
    #     game_over=True
    #     print("You win!")

    # print(stages[lives])


