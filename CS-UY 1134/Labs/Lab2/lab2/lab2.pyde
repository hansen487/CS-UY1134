sunLocation=(250,250)
sunRadius=50
yellow=(255,255,0)

earthRadius=30
blue=(0,0,255)
earthOrbitalRadius=170
earthSpeed=0.5

marsRadius=20
red=(255,0,0)
marsOrbitalRadius=80
marsSpeed=1

moonRadius=10
white=(255,255,255)
moonOrbitalRadius=45
moonSpeed=2.3

class Sun():
    def __init__(self, location, radius, color):
        self.location=location
        self.radius=radius
        self.color=color
        self.lst=[]
    def _getLocation(self, time):
        return self.location
    def draw(self, time):
        drawCelestialBody(self._getLocation(time), self.radius, self.color)
        for i in self.lst:
            i.draw(time)
    def addPlanet(self, radius, orbitalRadius, color, speed):
        planet=(Planet(radius, orbitalRadius, color, speed, self))
        self.lst.append(planet)
        return planet
   
class Planet(Sun):
    def __init__(self, radius, orbitradius, color, speed, revolve):
        self.radius=radius
        self.orbitradius=orbitradius
        self.color=color
        self.speed=speed
        self.revolve=revolve
        self.lst=[]
    def _getLocation(self, time):
        return getLocation(self.revolve._getLocation(time), self.orbitradius, self.speed, time)


def getLocation(orbitAroundLocation,orbitRadius,speed,time):
    centerX=orbitAroundLocation[0]+orbitRadius*sin(speed*time)
    centerY=orbitAroundLocation[1]+orbitRadius*cos(speed*time)
    return (centerX,centerY)

def drawCelestialBody(location,radius,color):
    fill(*color)
    locX,locY=location
    ellipse(locX,locY,radius*2,radius*2) 
       
sun=Sun(sunLocation, sunRadius, yellow)
earth=sun.addPlanet(earthRadius, earthOrbitalRadius, blue, earthSpeed)
sun.addPlanet(marsRadius, marsOrbitalRadius, red, marsSpeed)
earth.addPlanet(moonRadius, marsOrbitalRadius, white, moonSpeed) 
  
def setup():
    size(500,500)
    global t
    global Planets
    t=0

def draw():
    global t
    t+=.02
    background(0)
    sun.draw(t)      
    
    
    