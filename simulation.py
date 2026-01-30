
while (nb_tours < 500):
    for elem in moutons :
        elem.vieillir()
        elem.mort()
    for elem in loups :
        elem.vieilir()
        elem.mort()

    for elem in Grid :
        
