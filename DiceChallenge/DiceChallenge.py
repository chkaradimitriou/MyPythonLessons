import random

# Δημιουργία δύο ζαριών με τυχαίους αριθμούς 1-6 και εκτύπωση αποτελέσματος

dice1 = random.choice([1, 2, 3, 4, 5, 6])
print(dice1)

dice2 = random.choice([1, 2, 3, 4, 5, 6])
print(dice2)

if dice1 == dice2:
    print("Έφερες διπλές " + str(dice1) + " " + str(dice2))
else:
    print("Το πρώτο ζάρι έφερε " + str(dice1) + " και το δεύτερο " + str(dice2))