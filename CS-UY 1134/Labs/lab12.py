import random

def select(lst, k, levels=0):
    #print('\t'*levels+'Selecting',k,'in',lst)
    new_lst=[]
    fivelist = []
    counter = 0
    for i in lst:
        fivelist.append(i)
        counter += 1
        if counter == 5:
            new_lst.append(fivelist)
            fivelist = []
            counter = 0
    if fivelist != []:
        new_lst.append(fivelist)
    #if len(new_lst) > 1:
        #print('\t'*levels+'Groups:\t',new_lst)
    listofmedians = []
    for i in new_lst:
        i.sort()
        listofmedians.append(i[len(i)//2])
        #print(listofmedians)
    if len(lst) <= 5:
        #print('\t'*levels+'Short sequence, returning',new_lst[0][k])
        return new_lst[0][k]
    else:
        #print('\t'*levels+'Sorted groups: \t',new_lst)
        #print('\t'*levels+'Middles:\t', listofmedians)
        median = select(listofmedians, len(listofmedians)//2, levels+1)
        #print(median)
        small = []
        big = []
        for i in lst:
            if i < median:
                small.append(i)
            elif i > median:
                big.append(i)
        #print('\t'*levels+'Small/middleofmiddlse/big:',small,median,big)
        if len(small)>k:
            return select(small, k, levels+1)
        elif len(small) == k:
            #print('\t'*levels+'Short sequence, returning',median)
            return median
        else:
            return select(big, k-len(small)-1, levels+1)
    
    
#print(select([10,1,0,11,3,9,20,12,7,8,17,6,2,14,19,18,21,16,15,13,5,4],15))

A=list(range(222))
random.shuffle(A)
print([select(A,i) for i in range(222)])

