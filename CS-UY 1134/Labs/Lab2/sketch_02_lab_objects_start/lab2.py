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
    def __init__(self, location, radius, ycolor):
        self.location=location
        self.radius=radius
        self.ycolor=ycolor
    def _getLocation(self, time):
        getLocation(self.location, self.radius, self.speed, time)
    def draw(self):
        drawCelestialBody(self.location, self.radius, self.ycolor)
    def addPlanet(self, planetradius, orbitalRadius, planetcolor, speed):
        self.planetradius=planetradius
        self.orbitalRadius=orbitalRadius
        self.planetcolor=planetcolor
        self.speed=speed
'''    
class Planet():
    def __init__(self, revolve, radius, orbitradius, planetcolor, speed):
        self.sun=sun
        self.radius=radius
        self.orbitradius=orbitradius
        self.planetcolor=planetcolor
        self.speed=speed
        self.revolve=revolve
    def _getLocation(self, time):
        getLocation(self.revolve.location, self.revolve.radius, self.speed, time)
    def draw(self):
        drawCelestialBodyfill(self.location, self.radius, self.color)
'''
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
    
    
    