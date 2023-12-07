from random import randint
def dead_game():
    print("choisis un emplacement dans le barrilet entre 1 et 6")
    cartouche= int(input())
    if cartouche > 6:
        print ("eronné !")
        exit()
    balle= randint(1,6)
    while cartouche != balle:
        print ("gagné")
        cartouche= int(input())
        if cartouche > 6:
            print ("eronné !")
            exit()
        balle= randint(1,6)
    print("perdu!")

dead_game()