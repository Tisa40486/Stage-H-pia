


def python():
    switch=bool
    plateforme_social = ["Facebook","Snapchat","Instagram","Omegle"]
    print(plateforme_social)
    plateforme_social.append("Twitter") 
    print(plateforme_social)
    plateforme_social.remove("Snapchat")
    print(plateforme_social)
    print(len(plateforme_social))
#python()
def dictonnaire():
    nouvelle_campagne= {
        "chef de la campagne" : "Jeanne D'ARC",
        "nom de la campagne" : "nous aimons les chiens",
        "date de début" : "01.11.2020", 
        "influencer" : ["@toutpourlesToutous","@canininsta"]
    }
    print(nouvelle_campagne)
#dictonnaire()
def conversion_dict():
    taux_de_conversion= dict()
    taux_de_conversion["Facebook"] = 3.4 
    taux_de_conversion["Snapchat"] = 1.2
    print(taux_de_conversion)
#conversion_dict() 
def ensoleille():
    from random import randint
    meteo= randint(1,5)
    if meteo<2:
        print("sortons !")
    else:
        meteo>2
        print("restons a la maison")
#ensoleille()
def ma_fonction():
    a=10
    b=(5)
    ma_variable=(a*b)
    print(ma_variable)
#ma_fonction()
def liste():
    liste = [1,2,3,4,5,6,7,8]

    liste.remove(2)
    liste.remove(5)
    liste.remove(6)
    liste.append(9)
    liste.append(99)
    print(liste)
#liste()
def valeurs_retour(a,b):
    calcul= a + b 
    return calcul
valeurs_retour(a,b)