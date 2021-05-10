# if else | defterova9mia exiswsh + diakrinousa
import math

a = 1
b = 2
c = -9

d = (b * b) - 4 * a * c
x1 = -b + math.sqrt(d) / 2 * a
x2 = -b - math.sqrt(d) / 2 * a

if d > 0:
    print('Η εξίσωση έχει πάντα δύο ρίζες ' + str(x1))
    print('Η εξίσωση έχει πάντα δύο ρίζες ' + str(x2))
elif d == 0:
    x = - b / 2 * a
    print('Η εξίσωση έχει μια διπλή πραγματική ρίζα' + str(x))
else:
    print('Δεν μπορεί να ληθεί')
