print("largeur")
large=int(input())
print("longueur")
longueur=int(input())
def cellule_large_top():
   print(("╔")+(((("═")*2) + ("╦"))*(large-1))  + ("══╗"))
   (("═")*large)
cellule_large_top()
def cellule_long(): 
   for i in range(longueur):
      for j in range(large):
        print((("║") + ("B "))*(large)+"║", end="") 
        print(("╠") + ((("═")*2) + ("╬"))*(large-1) + ("══╣"))
cellule_long()
def cellule_large_bottom():
   print(("╚")+(((("═")*2) + ("╩"))*(large-1))  + ("══╝"))
   (("═")*large)
cellule_large_bottom()

