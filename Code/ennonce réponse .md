## Travail pratique 1

### 1. Python
1.1 Déclarer et instancier une variable au nom de `toto` et y assigner la valeur `100` 
```py
toto = 100
``` 

1.2 Déclarer et instancier une vaiable au nom de `liste` et y assigner une liste de **5** composants (sous forme de chaine de caractères) de PC (exemple `GPU`) 
```py
liste=["GPU","CPU","MOTHERBOARD","CARTE SON","CARTE WIFI"]
``` 

1.3 Déclarer et instancier une variable (peu importe son nom) contenant une chaine de caractères quelconque, celle-ci doit contenir au moins 6 caractères. 
```py
variable = "une chaine de caractères quelconque"
``` 

1.4 Répondre aux questions suivantes 
a. Que signifie **déclarer une variable** ?
b. Que signifie **instancier une variable** ?
c. Quelle est la différence entre **déclarer** et **instancier** une variable ?
```
a. Déclarer une variable signifie que l'on reserve une place pour la mémoire de la variable.
b. Instancier une variable signifie que la variable précise l'état de la valeur auxquelle elle se rèfère.
c. La différence est le fait de déclarer indique l'existence d'une variable sans en crée une, alors que instancier une variable revient à créer cette variable.
```

1.5 Donnez la définition du mot **itérer**
```
Une itération est une repétitions d'instructions dans le programme.
```

1.6 Donnez deux façon différentes d'itérer sur la liste suivante avec les boucles `for`
```py
liste = [100, 230, 7, -2, 99, 0, 52, 21, 140, -70]
- for nombres in liste 
- for nombres in range(len(liste))

``` 

1.7  Quelle est la synthaxe de base pour définir une fonction ? 
```py
 La syntaxe de base pour définir une fonction est def fonction():
``` 

1.8  Quel est le mot reservé en Python pour faire en sorte qu'une fonction **retourne** une valeur ?
```py
 return 
``` 

1.9 Expliquez le principer de **retour** dans une fonction.
```
Le principe de "retour" dans une fonction est de retourné une valeur à la fonction.
``` 

1.10 En imaginant que vous possedez un script Python nommé `script.py`. **Quelle ligne de commande** vous permets de l'executer, dans un terminal Linux ?
```bash
python3 script.py
``` 

1.11 Citez le plus de **types de données** que possible (minimum 4).
```python
- float
- int 
- str 
- bool 
```

1.12 Expliquez pourquoi ce script, une fois executé, **ne produit rien** dans le terminal.
```py
def ma_fonction():
    print("Salut !!!")


Car la fonction à pas été appellé avec ma_fonction()
```

1.13 Expliquez le concept de `commentaires` en informatique et indiquez avec quel symbole doit précédé un commentaire pour que Pyhton "l'interprète" en tant que tel.
```
Les commentaires servent à organiser et expliquer le programmer aux personnes qui l'utiliserons et/ou l'optimiserons #
```

1.14 Expliquez ce que la fonction `print()` permet de faire.
```
print() sert à afficher une chaine de caractéres ou des valeurs dans le terminal.
```

1.15 Selon vous, le code ci-dessous affichera t'il la valeur **15** dans le terminal ? 
```py
def ma_fonction(a, b):
    a*b

ma_variable = ma_fonction(10, 5)
print(ma_variable)

Non car le code va afficher la valeur 50 car * est une multiplication.
et les lignes de code ne sont pas aligné avec tabulation:
```

1.16 Réecrivez le code de la question `1.15` pour que celui-ci fonctionne
```py
def ma_fonction():
    a=(10)
    b=(5)
    ma_variable=(a*b)
    print(ma_variable)
ma_fonction()

```

1.17 Faites en sorte que le code présenté plus bas puisse produire la sortie suivante:
```
[1,3,4,7,8,9,99]
```
Le code a modifier (**ne pas modifier le code déjà présent**): 
```py
liste = [1,2,3,4,5,6,7,8]
    liste.remove(2)
    liste.remove(5)
    liste.remove(6)
    liste.append(9)
    liste.append(99)
    print(liste)
```


#### 2. Linux

**work in progress...**