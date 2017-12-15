def insomewhere(X, s):
    for item in X:
        if item == s:
            return True
        elif isinstance(item, list):
            if insomewhere(item, s) == True:
                return True
            else:
                return insomewhere(X[1:], s)
    return False
#A = [[1,2],[3,[[[4],5]],6],7,8]
#print(insomewhere(A, 6))
#print(insomewhere(A, 66))

def unnest(lst, X=[]):
    for item in lst:
        if isinstance(item, int):
            X.append(item)
        elif isinstance(item, list):
            unnest(item, X)
        return unnest(lst[1:], X)
    return X
#A=[[1,2],[3,[[[4],5]],6],7,8]
#print(unnest(A))
#print(A)

def print2d(A):
    print('[')
    for i in A:
        print(' '+str(i))
    print(']')
#print2d([i]*5 for i in range(5))
        
def triangle(x, tri = [], counter = 0):
    if x == 0 :
        return tri
    elif counter == 0:
        tri.append([x])
    else:
        tri.append(tri[counter-1]+[x])
    return triangle(x-1, tri, counter+1)
        
#print2d(triangle(5))  
#print2d(triangle(10))  

def table(f, A, x):
    output = []
    for i in x:
        row = [f(j, i) for j in A]
        output.append(row)
    return output
#print2d(table(pow,[1,2,10],range(10,15)))

def nest(item, x):
    if x == 0:
        return item
    else:
        return nest([item], x-1)
#print(nest(53,10))
#print(unnest(nest(53,10)))

A=[[1],[1]]*5
print(A)
A[3][0]=5
print(A)