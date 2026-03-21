easy_words = [
    "apple","bread","chair","plant","water","green","black","white","stone","light",
    "river","smile","laugh","house","floor","drink","sweet","mouse","train","cloud",
    "table","clock","heart","sugar","beach","grass","happy","dream","sound","sheep",
    "fruit","tiger","zebra","piano","radio","phone","shirt","pants","shoes","socks"
]
import random
gameOn = True
HANGMAN_PICS = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]
max_wrong = len(HANGMAN_PICS) - 1

print("Welcome to Hangman!")
wrong_guesses = 0
stage = wrong_guesses
print(HANGMAN_PICS[stage])
while gameOn:
    
    word = random.choice(easy_words)
    
    guess = input("Guess a letter: ")
    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        stage = wrong_guesses
        print(HANGMAN_PICS[stage])
        if wrong_guesses == max_wrong:
            print("Game Over!")
            gameOn = False
