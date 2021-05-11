# For Loop + list

list = ["apple", "banana", "melon", "apple", "cherry"]
print(list)

for x in list:
    print(x)

thislistint = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(thislistint)

for y in thislistint:
    print(y)

i = 0
while i < len(list):
  print(list[i])
  i += 1

j = 0
while j < len(thislistint):
    if j < 5:
        print(thislistint[j])
    j = j + 1
else:
    print("Το j είναι μεγαλύτερο από 5")
#while
#do while
#tropoi epanalipshs


