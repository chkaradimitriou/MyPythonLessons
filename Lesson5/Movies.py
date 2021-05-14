# create object "5 movies" - create movielist - print stoixeia twn tainiwn
from Lesson5.model.Car import Car
from Lesson5.model.Movie import Movie

# nissan 350z toyota supra mitsubishi evo 4 doors

nissan = Car("nissan", "350z", "2000", "2")
toyota = Car("toyota", "supra", "1992", "2")
evo = Car("mitsubishi", "evo", "1995", "4")

list = [nissan, toyota, evo]

print(list[1].manufacturer)

for i in list:
    print(i.manufacturer + " " + i.model + " " + i.releaseDate + " " + i.doors)

i = 0
while i < len(list):
    print(list[i].manufacturer + " " + list[i].model + " " + list[i].releaseDate + " " + list[i].doors)
    i += 1

print(type(nissan))

