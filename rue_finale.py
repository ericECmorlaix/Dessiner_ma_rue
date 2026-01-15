# Dépendances

from sol import sol
from immeuble import *

# Définitions


def rue_finale(canvas):
    
    # Affichage de ma rue
    affiche(canvas)
    
    
    # Dessin des immeubles
    for i in range(4):
        immeuble(i*rue.width/4+100)
        
    # Dessin du sol de la rue
    sol()
# Tests
if __name__ == '__main__':
    rue_finale(rue)