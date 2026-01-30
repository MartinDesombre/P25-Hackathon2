
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

        
