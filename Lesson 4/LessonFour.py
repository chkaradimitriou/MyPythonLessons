name = 'Stathis'
print('My name is ' + name)

age = 25
print('O ' + name + ' einai ' + str(age) + ' xronwn')

coffeePrice = 1.70
print('O ' + name + ' pou einai ' + str(age) + ' xronwn' + 'pire kafe kai plhrwse ' + str(coffeePrice))
'''
print('Dose ton ari9mo')
number = int(input())

def evenOrOdd(number):
    if (number % 2) == 0:
        print("{0} is Even".format(str(number)))
    else:
        print("{0} is Odd".format(str(number)))

evenOrOdd(number)

def Hello(name):
    print('Hello ' + name + '!')

Hello(name)
'''

shoppingList = ["Madarinia", "Axladia", "Portokalia"]
print(shoppingList)

for i in shoppingList:
    print(i)

i = 0
while i < len(shoppingList):
    print(shoppingList[i])
    i += 1
