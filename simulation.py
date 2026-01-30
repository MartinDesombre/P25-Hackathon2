from mouton import Mouton
from loup import Loup
import random

while (nb_tours < 500):
       


    for mouton in moutons :
        if mouton._en-vie :
            mouton.vieillir()

            if mouton.trouve_herbe()[0]:
                mouton.deplace(mouton.trouve_herbe[1:2])
                grille_herbe[mouton.x][mouton.y].mangee()
                mouton.manger()
            else :
                mouton.deplace(direction_aleatoire)
            
            if mouton.energie > 50 :
                mouton.reproduction()
            mouton.energie += -1




    for loup in loups :
        loup.vieilir()

        if loup.trouve_mouton():
            loup.bouge_mouton()

            #mouton_trouve = trouver l'id du mouton bouffé

            mouton_trouve.mangee()

        loup.mort()

    for mouton in moutons :
        mouton.mort()
    for loup in loups:
        loup.mort
    grid.update()
        



def generer_coordonnees_uniques(nombre, taille_grille):
    toutes_les_positions = [(x, y) for x in range(taille_grille) for y in range(taille_grille)]
    coordonnees = random.sample(toutes_les_positions, nombre)
    return coordonnees

positions_jeu = generer_coordonnees_uniques(60, 30)

moutons= [Mouton(positions_jeu[i]) for i in range(50)]
loups= [Loup(positions_jeu[i]) for i in range(10)]