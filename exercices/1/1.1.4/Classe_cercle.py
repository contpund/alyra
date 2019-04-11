class Cercle(object):
    def __init__(self, Radius = 0 ):
       import math
       self.pi = math.pi
       self.Radius = Radius
    
    def aire(self):
       return self.pi*(self.Radius) ** 2
    def perimetre(self):
       return 2 * self.pi * self.Radius

