# creer une nouvelle liste qui contient my_list, mais a l'envers
# en utilisant une boucle (sans utiliser reverse)

my_list = [1,2,3,4,5,6,7,8,9,10]
size = len(my_list)
new_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(my_list)

for index in range(size):
    new_list[size-1 - index] = my_list[index]


print(new_list)

