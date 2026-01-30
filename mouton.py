from random import *


moutons = {}
class Mouton : 
    def _init_ (self, x, y) : 
        self._x = x
        self._y = y
        self._age = 0    
        self._energie = 20
        self._en-vie = True
    
    def vieillir (self) :
        self._age += 1
    
    def trouve_herbe (self) :
        if Grid.cells[self._x+1][self._y] == '#' : 
            return (True, 1, 0)
        if Grid.cells[self._x][self._y+1] == '#' : 
            return (True, 0, 1)
        if Grid.cells[self._x-1][self._y] == '#' : 
            return (True, -1, 0)
        if Grid.cells[self._x][self._y-1] == '#' : 
            return (True, 0, -1)
        return (False,0,0)
    
    def direction_aleatoire (self):
        a = random.randint (1,4)
        if (a == 1 and self._x + 1 <=30):
            return (1,0)
        elif (a == 2 and self._y + 1 <= 30) :
            return (0,1)
        elif (a == 3 and self._x -1 >=0):
            return(-1,0)
        elif (a == 4 and self._y -1 >=0):
            return (0,-1)

    def deplace (self,dx,dy) :
        self._x += dx
        self._y += dy
        
    
    def manger (self) :
        self._energie += 10

    def reproduction (self) : 
        if self._energie > 50 :
            self._energie += -20
        dx,dy = Grid.case_vide(self._x,self._y)
        moutons[len(moutons)]= Mouton(self._x + dx, self._y + dy)

    def mort (self) :
        if self._energie <= 0 :
            self._en-vie = False
        if self._age > 50 :
            self._en-vie = False


        

    
    