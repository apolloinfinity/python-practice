"""
This Python file may seem insignificant but I created it to show aspiring Python developers about workflow and implementin, 
while loop, elif and using the input. The try

"""

while True:
    a = input("Choose a, b, or c or type q to quit ")
    if a == "a":
        print('You chose AAAAAA')
    elif a == "b":
        print('You chose BBBBBBB!!')
    elif a == "c":
        print("Ciao")
    elif a == "q":
        print("Goodbye")
        break
    else:
        print("Choose one of the options")
    
    