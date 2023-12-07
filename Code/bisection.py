def f(x):
     # methode de calcul(x)-> return x
    return 3.5*x+0.9 
def mid(a1,b1):
    # methode millieu de la courbe (a,b)-> return (a+b)/2
    millieu= (a1+b1)/2
    return millieu 
def est_positif(a1):
#méthode de positif/négatif avec booléen
    if a1>=0:
        a1=True
#true est positive
    elif a1<0:
        a1=False
#false est négatif
    return a1 

def algo():
    a= -10
    b= 20
    c=mid(a,b)
    
    while abs(f(c))>0.000000001:
        c=(a+b)/2
        if est_positif(f(a))==est_positif(f(c)):
            a=c 
        else: 
            b=c 
    print("la valeur est ", c)
    print("Ce qui donne ", f(c))

algo()
            