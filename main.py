from random import *


moutons = []
class Mouton : 
    def _init_ (self, x, y) : 
        self._x = x
        self._y = y
        self._age = 0    
        self._energie = 20
        self._en-vie = True
    
    def detecter_herbe (self) :

    
    def deplace (self) :
        a = random.randint (1,4)
        if a == 1 :
            self._x += 1
        elif a == 2 :
            self._y += 1
        elif a == 3 :
            self._x += -1
        elif a == 4 :
            self._y += -1
    
    def manger (self) :
        self._energie += 10

    def reproduction (self) : 
        if self._energie > 50 :
            self._energie += -20

            moutons[len(moutons)]= Mouton()

    def mort (self) :
        if self._energie <= 0 :
            self._en-vie = False
        if self._age > 50 :
            self._en-vie = False
        

    
    