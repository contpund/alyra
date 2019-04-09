from math import *

List = list(range(1, 100))

try:
    Solution = int(input('Entrez un nombre de 1 à 100: '))
except ValueError:
        print("Entrez un chiffre")

if Solution < 1 or Solution > 100:
        print(" Valeur à choisir entre 1 et 100")
Try = 0
    
i = 0
Len = len(List)
Dictoto = floor(( i + Len)/2)

while i < Len:
    if Solution == List[Dictoto]:
        print("résultat = ",List[Dictoto])
        break
    
    elif Solution > List[Dictoto]:
        i = Dictoto
        Try = Try + 1        
        print("Tentative",Try," :",Dictoto)
    else:
        Len = Dictoto
    Dictoto = floor((i+Len)/2) 
