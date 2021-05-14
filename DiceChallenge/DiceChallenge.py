import random
from tkinter import *

tk = Tk()
tk.title("Roll The Dice")
tk.geometry("650x500")

description = Text(tk, height=1, )
description.insert(INSERT, 'GAME ON! Click the button to roll the dice.'.center(80))
description["state"] = DISABLED
description.pack()


def createResultText(result):
    results = Text(tk, height=1, )
    results.insert(INSERT, result.center(80))
    results["state"] = DISABLED
    results.pack()

# Δημιουργία δύο ζαριών με τυχαίους αριθμούς 1-6 και εκτύπωση αποτελέσματος
def rollDice():
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    print(dice1)

    dice2 = random.choice([1, 2, 3, 4, 5, 6])
    print(dice2)

    if dice1 == dice2:
        result = 'Διπλές! Πρώτο Ζάρι : {0}, Δεύτερο Ζάρι : {1}'.format(dice1, dice2)
        createResultText(result)
    else:
        result = 'Έφερες τα εξής : Πρώτο Ζάρι : {0}, Δεύτερο Ζάρι : {1}'.format(dice1, dice2)
        createResultText(result)

button = Button(tk, text="Roll the dice", command=rollDice)
button.pack()

mainloop()
