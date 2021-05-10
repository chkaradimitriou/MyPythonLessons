# if else | defterova9mia exiswsh + diakrinousa
import math

print('Δώστε το Α')
a = int(input())

print('Δώστε το Β')
b = int(input())

print('Δώστε το C')
c = int(input())

d = (b * b) - 4 * a * c

if d > 0:
    x1 = -b + math.sqrt(d) / 2 * a
    x2 = -b - math.sqrt(d) / 2 * a
    print('Η εξίσωση έχει πάντα δύο ρίζες ', "{:.2f}".format(x1))
    print('Η εξίσωση έχει πάντα δύο ρίζες ', "{:.2f}".format(x2))
elif d == 0:
    x = - b / 2 * a
    print('Η εξίσωση έχει μια διπλή πραγματική ρίζα' + "{:.2f}".format(x))
else:
    print('Δεν μπορεί να ληθεί')