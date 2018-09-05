import math

class Point:
    def __init__(self,x,y):
        self.pierwsza=x
        self.druga=y

    def distance(self,punkt1):
        return (math.sqrt(((self.pierwsza-punkt1.pierwsza)**2 + self.druga-punkt1.druga)))

class Circle:
    def __init__(self,o,r):
        self.srodek=o
        self.promien=r

    def area(self,srodek,promien):
        return (2*math.pi*self.promien)

    def pointincircle(self,punkt):
        if self.promien >= self.distance(punkt):
            return True
        else:
            return False

    def collision(self,okrag):
        kolizja=False
        if self.promien+okrag.promien >= self.srodek.distance(okrag,srodek):
            if (self.promien <= okrag.promien):
                pomoc=Circle(okrag.srodek,okrag.promien-self.promien)
                if pomoc.pointincircle(srodek):
                    kolizja=True
            elif (self.promien > okrag.promien):
                pomoc=Circle(self.srodek,self.promien-okrag.promien)
                if pomoc.pointincircle(okrag,srodek):
                    kolizja=True
        return kolizja

punkciki=Point(0,0)
punkciki2=Point(2,3)
dystans=punkciki.distance(punkciki2)
print(dystans)

kolizja=collision
