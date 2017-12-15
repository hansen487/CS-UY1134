import random
global count
global state

#1 is dead, 2 is alive
def drawGrid(state):
    black=(0,0,0)
    white=(255,255,255)
    stroke(*black)
    global count
    global state
    if count==0:
        for i in range (50):
            state.append([])
            for j in range(50):
                x=random.randint(1,2)
                if x==2:
                    fill(*white)
                else:
                    fill(*black)
                rect(i*20+1, j*20+1, 20, 20)
                state[i].append(x)
    nextstate=[]
    for i in range(len(state)):
        nextstate.append([])
        for j in range(len(state[i])):
            print(state[i][j])
            data=readGrid(state, i, j)
            if data[0]==5:
                if state[i][j]==1:
                    nextstate[i].append(2)
                else:
                    if data[1]<2:
                        nextstate[i].append(1)
            else:
                if data[1]==2 or data[1]==3:
                    nextstate[i].append(2)
                else:
                    nextstate[i].append(1)
        for i in range (len(nextstate)):
            for j in range(len(nextstate[i])):
                if nextstate[i][j]==2:
                    fill(*white)
                else:
                    fill(*black)
                rect(i*20+1, j*20+1, 20, 20)
        state=nextstate

def readGrid(array, x, y):
    neighbor=[0,0,0,0,0,0,0,0,0]
    if x==0:
        neighbor[0]=-1
        neighbor[1]=-1
        neighbor[2]=-1
    elif x==49:
        neighbor[6]=-1
        neighbor[7]=-1
        neighbor[8]=-1
    if y==0:
        neighbor[0]=-1
        neighbor[3]=-1
        neighbor[6]=-1
    elif y==49:
        neighbor[2]=-1
        neighbor[5]=-1
        neighbor[8]=-1
    count=0
    print(neighbor)
    for i in range(3):
        for j in range(3):
            if neighbor[count]!=-1:
                if count!=4:
                    neighbor[count]=array[x-1+i][j-1+j]
                count+=1
    negonecount=0
    for i in neighbor:
        if i==-1:
            negonecount+=1
    alivecount=0
    for i in range (8):
        if neighbor[i]==2:
            alivecount+=1
    return (negonecount, alivecount)
    
    

# def keyPressed():
#     spacebar=True
#     return spacebar

def setup():
    size(1000,1000)
    background(255)
    global count
    count=0
    global state
    state=[]
    
def draw():
    global count
    global state
    state=drawGrid(state)
    count+=1