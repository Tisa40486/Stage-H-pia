import random


def GenerateMap(x_size, y_size, nb_bombs):
#generer la map
    map = []
    y = ((['O'])*y_size)
    for _ in range(x_size):
        map.append(y.copy())
    for _ in range(nb_bombs):
        ybomb=random.randint(0, len(map[0])-1)
        xbomb=random.randint(0, len(map)-1)
        map[xbomb][ybomb] = '💣'
    return map


def print_map(map):
    # debrouille toi pour afficher la map correctement ;)
    for e in map:
        print(' '.join(e))


def create_matrice(x_size, y_size):
    #création de la matrice
    matrice=[]
    for y in range(y_size):
        ligne=[]
        for x in range(x_size):
            ligne.append(False)
        matrice.append(ligne.copy())
    return matrice 


def print_matrice(matrice):
    #affichage matrice
    for ligne in matrice:
        for e in ligne:
            print(e, end='\t')
        print()

def bomb_random(max_y, max_x):
    #generation des bombes
    rand_x=random.randint(0, max_x)
    rand_y=random.randint(0, max_y)
    return rand_x, rand_y 

def fill_bomb_matrice(matrice, max_bomb):
    #ajout des bombes dans la matrice
    x_size=len(matrice)-1
    y_size=len(matrice[0])-1
    
    for _ in range(max_bomb):
        bomb_x, bomb_y = bomb_random(y_size, x_size)
        matrice[bomb_x][bomb_y]=True

def create_revetement(x_size, y_size):
    #creer un revetement de la matrice
    matrice_revet=[]
    for y in range(y_size):
        ligne=[]
        for x in range(x_size):
            ligne.append("|❌|")
        matrice_revet.append(ligne.copy())
    return matrice_revet

def print_matrice_revet(revetement):
    for i in range(len(revetement)):
        for j in range(len(revetement [i])):
          print(revetement[i][j], end='')
        print()


def create_matrice_openclose(x_size, y_size):
    #création de la matrice open/close
    matrice=[]
    for y in range(y_size):
        ligne=[]
        for x in range(x_size):
            ligne.append(False)
        matrice.append(ligne.copy())
    return matrice 