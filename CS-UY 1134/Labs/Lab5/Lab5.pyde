
class Disc():
    def __init__(self, x, y, w, h):
         self.height = h
         self.width = w
         self.x = x
         self.y = y
    def getsize(self):
        self.size = self.width*self.height
        return self.size
    def drawdisc(self):
          fill(255)
          rect(self.x, self.y, self.width, self.height)   

class Tower():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.discs = []
    def push(self, x, y, w, h):
        self.x = x
        self.y = y
        self.discs.append(Disc(self.x, self.y, w, h))
    def pop(self):
        return self.discs.pop()
    def top(self):
        return self.discs[len(self.discs)-1]
    def getdiscs(self):
        return self.discs
    def draw(self):
        stroke(142)
        strokeWeight(8)
        line(self.x1, self.y1, self.x2, self.y2)
        strokeWeight(1)
        stroke(0)
        global disc1
        for disk in self.discs:
            disk.drawdisc()


t1x = 300
t2x = 900
t3x = 1500
y1 = 900
y2 = 400
Tower1 = Tower(t1x, y1, t1x, y2) 
Tower2 = Tower(t2x, y1, t2x, y2)
Tower3 = Tower(t3x, y1, t3x, y2)
h = 45
w = 400
global dx1
dx1 = t1x
global dx2
dx2 = t2x
global dx3
dx3 = t3x
global dy1
dy1 = 900
global dy2
dy2 = 900
global dy3
dy3 = 900
for i in range(10):
    global dx1
    global dy1
    Tower1.push(dx1, dy1, w, h)
    w -= 40
    dy1 -= h
global disc
disc = 'empty'
print(Tower3.getdiscs)
def keyPressed():
    if key == "1":
        global disc
        if disc == 'empty':
            disc = Tower1.pop()
            global dy1
            dy1 += h
            global origin
            origin = Tower1
        elif disc != 'empty':
            global dx1
            global dy1
            if Tower1.getdiscs() == []:
                Tower1.push(dx1, dy1, disc.width, disc.height)
                dy1 -= h
                disc = 'empty' 
            else:
                disc2 = Tower1.top()
                if disc.getsize()<disc2.getsize():
                    Tower1.push(dx1, dy1, disc.width, disc.height)
                    dy1 -= h
                    disc = 'empty'            
    if key =='2':
        if disc != 'empty':
            global disc
            global dx2
            global dy2
            if Tower2.getdiscs() == []:
                Tower2.push(dx2, dy2, disc.width, disc.height)
                dy2 -= h
                disc = 'empty'
            else:
                disc2 = Tower2.top()
                if disc.getsize()<disc2.getsize():
                    Tower2.push(dx2, dy2, disc.width, disc.height)
                    dy2 -= h
                    disc = 'empty'
        elif disc == 'empty':
            disc = Tower2.pop()
            global dy2
            dy2 +=h
            global origin
            origin = Tower2
    if key =='3':
        if disc != 'empty':
            global disc
            global dx3
            global dy3
            if Tower3.getdiscs() == []:
                Tower3.push(dx3, dy3, disc.width, disc.height)
                dy3 -= h
                disc = 'empty'
            else:
                disc2 = Tower3.top()
                if disc.getsize()<disc2.getsize():
                    Tower3.push(dx3, dy3, disc.width, disc.height)
                    dy3 -= h
                    disc = 'empty'
        elif disc == 'empty':
            disc = Tower3.pop()
            global dy3
            dy3 +=h
            global origin
            origin = Tower3
    
def setup():
    size(1800,1000)
    rectMode(CENTER)
    
def draw():
    background(255)
    fill(0)
    rect(900, 950, 1800, 100)
    Tower1.draw()
    Tower2.draw()
    Tower3.draw()