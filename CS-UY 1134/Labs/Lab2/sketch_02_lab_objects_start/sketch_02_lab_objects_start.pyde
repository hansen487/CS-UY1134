


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


def getLocation(orbitAroundLocation,orbitRadius,speed,time):
    centerX=orbitAroundLocation[0]+orbitRadius*sin(speed*time)
    centerY=orbitAroundLocation[1]+orbitRadius*cos(speed*time)
    return (centerX,centerY)

def drawCelestialBody(location,radius,color):
    fill(*color)
    locX,locY=location
    ellipse(locX,locY,radius*2,radius*2)    
    

def setup():
    global t
    size(500,500)
    t=0
    
def draw():
    global t
    t+=0.02
    background(0)
    
    #Sun
    drawCelestialBody(sunLocation,sunRadius,yellow)

    #Earth
    earthLocation=getLocation(sunLocation,earthOrbitalRadius,earthSpeed,t)
    drawCelestialBody(earthLocation,earthRadius,blue)
    
    #Mars
    marsLocation=getLocation(sunLocation,marsOrbitalRadius,marsSpeed,t)
    drawCelestialBody(marsLocation,marsRadius,red)
    
    #Moon
    moonLocation=getLocation(earthLocation,moonOrbitalRadius,moonSpeed,t)
    drawCelestialBody(moonLocation,moonRadius,white)
    