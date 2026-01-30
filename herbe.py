import random
import numpy as np



class Herbe():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tps_depuis_mort = -1 if random.random() <= 0.3 else random.randint(0,7)
        # si tps_depuis_mort = -1, l'herbe est vivante
        # si tps_depuis_mort = 0, l'herbe vient d'être mangée
        # si tps_depuis_mort > 0, tps_depuis_mort represente le nombre de tours depuis la mort
    
    def mangee(self):
        self.tps_depuis_mort = -1

    def repousse(self):
        if is_mouton(self.x, self.y):
            pass  # Ne rien faire s'il y a un mouton
        else:
            if self.tps_depuis_mort == -1:
                pass  # L'herbe est deja vivante, ne rien faire
            else:
                self.tps_depuis_mort += 1  # on actualise le tps depuis la mort

            # Vérifier si l'herbe doit repousser
            if random.random() < 0.08 or self.tps_depuis_mort >= 7:
                self.tps_depuis_mort = -1  # Réinitialiser le temps depuis la mort
