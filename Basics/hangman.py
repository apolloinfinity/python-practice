def hangman(word):
    wrong = 0
    stages = stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__" * len(word)
    win = false
    print("Welcome to Hangman")


while wrong < len(stages) - 1:
    print("\n")
    msg = "Guess a letter"
    char = input(msg)
    if char in rletters:
        cind = rlettes \
             .index(char)
        board[cind] = char
        rletters[cind] = '$'
    else:
        wrong += 1
        print
