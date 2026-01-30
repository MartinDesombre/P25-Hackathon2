
while (nb_tours < 500):
       


    for mouton in moutons :
        mouton.vieillir()

        if mouton.trouve_herbe():
            mouton.bouge_herbe()
            grille_herbe[mouton.x][mouton.y].mangee()


        mouton.mort()


    for loup in loups :
        loup.vieilir()

        if loup.trouve_mouton():
            loup.bouge_mouton()

            #mouton_trouve = trouver l'id du mouton bouffé

            mouton_trouve.mangee()

        loup.mort()

    grid.update()
        
