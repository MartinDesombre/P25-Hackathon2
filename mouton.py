from random import *


moutons = {}
class Mouton : 
    def __init__ (self, x, y) : 
        self.x = x
        self.y = y
        self.age = 0    
        self.energie = 20
        self.vivant = True
    
    def vieillir (self) :
        self.age += 1
    
    def trouve_herbe (self) :
        if Grid.cells[self.x+1][self.y] == '#' : 
            return (True, 1, 0)
        if Grid.cells[self.x][self.y+1] == '#' : 
            return (True, 0, 1)
        if Grid.cells[self.x-1][self.y] == '#' : 
            return (True, -1, 0)
        if Grid.cells[self.x][self.y-1] == '#' : 
            return (True, 0, -1)
        return (False,0,0)
    
    def direction_aleatoire (self):
        a = random.randint (1,4)
        if (a == 1 and self.x + 1 <=30):
            return (1,0)
        elif (a == 2 and self.y + 1 <= 30) :
            return (0,1)
        elif (a == 3 and self.x -1 >=0):
            return(-1,0)
        elif (a == 4 and self.y -1 >=0):
            return (0,-1)

    def deplace (self,dx,dy) :
        self.x += dx
        self.y += dy
        
    
    def manger (self) :
        self.energie += 10

    def reproduction (self) : 
        if (self.energie > 50 and Grid.case_vide(self.x,self.y)[0]):
            self.energie += -20
            dx,dy = Grid.case_vide(self.x,self.y)[1:2]
            moutons[len(moutons)]= Mouton(self.x + dx, self.y + dy)

    def mort (self) :
        if self.energie <= 0 :
            self.vivant = False
        if self.age > 50 :
            self.vivant = False


        

    
    