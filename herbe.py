import random
import numpy as np



class Herbe():
    def __init__(self,x,y,tps_depuis_mort):
        self.x = x
        self.y = y
        self.tps_depuis_mort = 0 if random.random() <= 0.3 else random.randint(1,7)
    
    def mangee(self):
        Grille.herbe(self.x,self.y) = 0

    def repousse(self):
        if is_mouton(self.x,self.y) or self.tps_depuis_mort == 0:
            pass
        elif random.random() < 0.08 :
            self.tps_depuis_mort = 0
        
        elif tps_depuis_mort >= 7:
            self.tps_depuis_mort = 0
