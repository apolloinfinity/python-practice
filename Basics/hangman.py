import random


def hangman(word):
    wrong = 0
    stages = [""
              "______     ",
              "           ",
              "     |     ",
              "     0     ",
              "    /|\    ",
              "    / \    ",
              "           "
              ]
    rletters = list(word)  # remaining letters left to be guessed.
    board = ["__"] * len(word)  # keeps track of length of word and
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters \
                .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! The word was {}".format(word))


randomList = ['cat','butt','nut','shut','up','kill','killa','kill','yo']
randomChoice = random.choice(randomList)
#print(randomChoice)
hangman(randomChoice)
