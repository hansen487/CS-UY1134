import sys
import random
import math


def setup():
    size(2000, 2000)
    background(255)
    pixelDensity(displayDensity())

def drawLineAngle(start, angle, length, width, color=(0,0,0)):
    angle += 180 # make up zero degrees
    end = (start[0] + math.sin(math.radians(angle)) * length, start[1] + math.cos(math.radians(angle)) * length)
    stroke(*color)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end

def drawLeaf(location):
    stroke(0, 50, 0)
    fill(100, 255, 100)
    strokeWeight(0.5)
    ellipse(location[0],location[1],10,10)
    
def drawTree(start, leaf, angle=30, length=75, counter=0, end=0, width=10):
    if counter<10:
        if counter==0:
            end = drawLineAngle(start,0,200, width)
            endL = drawLineAngle(end,angle,length-5, width/1.25)
            endR = drawLineAngle(end,-angle,length-5, width/1.25)
            #drawLeaf(end)
            #fill(0,0,0)
            #global vertnum
            #text(vertnum, end[0], end[1])
            #vertnum+=1
        else:
            endL = drawLineAngle(end,angle,length-5, width)
            endR = drawLineAngle(end,angle-2*30,length-5, width)
            #drawLeaf(end)
            #fill(0,0,0)
            #text(vertnum, end[0], end[1])
            #vertnum+=1
        counter+=1
        drawTree(endL, leaf, angle+30, length-5, counter, endL, width/1.25)
        drawTree(endR, leaf, angle-30, length-5, counter, endR, width/1.25)
    else:
        if leaf:
            drawLeaf(end)
            #fill(0,0,0)
            #text(vertnum, end[0], end[1])
            #vertnum+=1
            
        
def keyPressed():
    global leaf
    if key=="l":
        leaf = not leaf
        
def setup():
    global vertnum
    vertnum=0
    global leaf
    leaf=True
    
def draw():
    global vertnum
    vertnum=0
    clear()
    background(255)
    drawTree((550,800),leaf)