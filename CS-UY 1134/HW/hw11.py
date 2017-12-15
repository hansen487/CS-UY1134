from heapq import heapify, heappop

class Passenger:
    def __init__(self, first, last, status, fare, bags):
        self._first_name = first
        self._last_name = last
        self._status = status
        self._fare = fare
        self._bags = bags
        self._boardtime = None
    def __lt__(self, other):
        self.statuses = {"None": 0, "Silver": 1, "Gold": 2, "Platinum": 3, "1K": 4, "Global Services": 5, "Employee": 6}
        if self.statuses[self._status] != self.statuses[other._status]:
            return self.statuses[self._status] < self.statuses[other._status]
        else:
            if self._bags != other._bags:
                return self._bags < other._bags
            else:
                if self._fare != other._fare:
                    return self._fare < other._fare
                else:
                    return other._boardtime < self._boardtime  
                
    #I don't see a need for __eq__, so I didn't code it. even if everything else is the same, boarding time will never be the same.

class Flight:
    def __init__(self, capacity):
        self._data = []
        self._capacity = capacity
        self._size = 0
        self._finalize = False
        self._removed = []
        
    def _isempty(self):
        return len(self._data) == 0
        
    def __len__(self):
        return len(self._data)
    
    def board(self, passenger):
        if self._finalize == False:
            self._data.append(passenger)
            passenger._boardtime = len(self._data)
            
    def finalize(self):
        if self._finalize == False:
            self._finalize = True
            heapify(self._data)
            
    def whoToRemove(self):
        if self._finalize == True:
            while len(self._data)>self._capacity:
                self._removed.append(heappop(self._data))
            return self._removed
        
    def __iter__(self):
        for i in self._data:
            yield (i._first_name)

#following code tests for removing when only baggage differs, same status but different fare, and same everything but different board times
UA3411=Flight(5)
john=Passenger("John","Iacono","Platinum",532,1)
hansen=Passenger("Hansen", "Chen","1K",245, 1)
jason=Passenger("Jason","Lau","Platinum",533,1)
gus=Passenger("Gus","Person","None",100,0)
sai=Passenger("Sai","Kalakota","None",100,1)
brandon=Passenger("Brandon","Lam","1K",245,1)
employee1=Passenger("Employee","1","Employee",0,0)
employee2=Passenger("Employee","2","Employee",0,0)
employee3=Passenger("Employee","3","Employee",0,0)
employee4=Passenger("Employee","4","Employee",0,0)
UA3411.board(john)
UA3411.board(hansen)
UA3411.board(jason)
UA3411.board(gus)
UA3411.board(sai)
UA3411.board(brandon)
UA3411.board(employee1)
UA3411.board(employee2)
UA3411.board(employee3)
UA3411.board(employee4)
UA3411.finalize()
for i in UA3411:
    print(i, end=' ')
print()
dragList=UA3411.whoToRemove()
for i in dragList:
    print(i._first_name, i._last_name, i._status, i._fare, i._bags)
    
#following code tests if anyone gets removed if flight isn't full
UA3412=Flight(5)
bob=Passenger("Bob","Dylan","1K",300,3)
UA3412.board(bob)
UA3412.finalize()
dragList=UA3412.whoToRemove()
print(dragList)

