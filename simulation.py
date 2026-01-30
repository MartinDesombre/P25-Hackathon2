from mouton import Mouton
from loup import Loup
import random

import main.py as main



def trouver_mouton(x,y):
    for mouton in moutons:
        if mouton.x == x and mouton.y == y:
            return mouton





nb_tours = 0

while nb_tours < 500:
       


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
            grid.update()



    for loup in loups :

        loup.vieilir()
        loup.perte_energie()
        

        loup.deplacement()

        loup.reproduction()
        loup.mort()


        grid.update()
    

    vectorized_repousse(grille_herbe)
    grid.update()

    nb_tours += 1

        



def generer_coordonnees_uniques(nombre, taille_grille):
    toutes_les_positions = [(x, y) for x in range(taille_grille) for y in range(taille_grille)]
    coordonnees = random.sample(toutes_les_positions, nombre)
    return coordonnees

positions_jeu = generer_coordonnees_uniques(60, 30)

moutons= [Mouton(positions_jeu[i]) for i in range(50)]
loups= [Loup(positions_jeu[i]) for i in range(10)]