import random
import time

from map import *


def position():
    print("choisissez la positions de la case")
    print("[longueur....]")
    x=int(input())
    print("[largeur....]")
    y=int(input())
    return y, x

def put_flag(revetement, y, x):
    print(f"drapeau posé sur la case [{y},{x}]")
    revetement[y][x]="|⛳ |"

def remove_flag(revetement, y, x):
    print(f"drapeau enlevé sur la position[{y},{x}] Attention !")
    revetement[y][x]="|❌|"


def start_game(ma_matrice, revetement):
    #trois valeurs possible (open, hide, flag)
    win = False

    while not win:
        print_matrice_revet(revetement)
        x,y = position()
        print(f"Que voulez vous faire sur la position [{y},{x}]: \n[1=drapeau]\n[2=montrer la case]")
        action = int(input())
        if action == 1:
            print(f"que voulez vous faire avec le drapeau en [{y},{x}]?: \n[1=poser le drapeau]\n[2=enlever le drapeau]")
            action1= int(input())
            if action1 ==1:
                put_flag(revetement, y, x)
            elif action1 ==2:
                remove_flag(revetement, y, x)
            else:
                print("Code d'action non reconnu. Reessayez…")
        elif action ==2:
            reveal(ma_matrice, revetement, y, x)
        else:
            print("Code d'action non reconnu. Reessayez…")


def show_case(ma_matrice, revetement, y, x):
    #revetement[y][x] = "  "
    if ma_matrice[y][x] == True:
        revetement[y][x]="|💣|"
        print("une mine, perdu !")
        print_matrice_revet(revetement)
        input()
        exit()

    else:
        nombre(ma_matrice, revetement, y, x)

def nombre(ma_matrice, revetement, y, x):
        compteur=0
        for i in range(-1, 2):
            for j in range(-1, 2):
                ny= y + i
                nx= x + j
                if ny < 0 or ny >= len(ma_matrice):
                    continue
                if nx < 0 or nx >= len(ma_matrice[0]):
                    continue
                if ma_matrice[ny][nx] == True:
                    compteur += 1

        revetement[y][x] = f"|{compteur} |"

def reveal(ma_matrice, revetement, y, x):
    if revetement[y][x] != "|❌|":
        return
    show_case(ma_matrice, revetement, y, x)
    if revetement[y][x]== "|0 |":
        for i in range(-1, 2):
            for j in range(-1, 2):
                ny= y + i
                nx= x + j
                if ny < 0 or ny >= len(ma_matrice):
                    continue
                if nx < 0 or nx >= len(ma_matrice[0]):
                    continue
                reveal(ma_matrice, revetement, ny, nx)

