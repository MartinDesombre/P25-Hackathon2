
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
        
