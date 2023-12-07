from map import *
from action import *

def main():
    ma_matrice=create_matrice(10, 8)
    #print_matrice(ma_matrice)
    fill_bomb_matrice(ma_matrice, 10) 
    print()
    #print_matrice(ma_matrice)
    revetement=create_revetement(8, 10)
    print("grille de 8:10, 10 mines. les premieres cases commencent par zero.")
    print("bonne chance !")
    start=start_game(ma_matrice, revetement)


if __name__ == '__main__':
    main()