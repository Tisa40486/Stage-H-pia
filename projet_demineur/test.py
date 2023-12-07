from action import *

def nombre(ma_matrice, revetement, y, x):
#nombres de bombes au alentours
        compteur=0
        for i in range(-1, 2):
            #boucles principales
            for j in range(-1, 2):
                #boucles de la boucles
                ny= y + i
                # ny = position case vertical
                nx= x + j
                # nx = position case latéral
                if ny < 0 and ny >= len(ma_matrice):
                #condition pour les positions vertical/out of grind
                    continue
                if nx < 0 and nx >= len(ma_matrice[0]):
                    #condition pour les positions horizontal/out of grind
                    continue
                if ma_matrice[ny][nx] == True:
                    #bombe trouvé dans les cases alentours
                    show_case(ma_matrice, revetement, y, x)
        revetement[y][x] = compteur



def factorial(ma_matrice, revetement, y, x):
     for i in range(-1, 2):
            for j in range(-1, 2):
            show