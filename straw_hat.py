'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap,comp1

class StrawHatTreasury:

    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        self.crewmates=Heap(comp1,[])
        self.free_crewmates=self.fn(m)
        self.pseudo_free=[]
        self.completed_treasures=[]

    def fn(self,m):
        a=[]
        for i in range(m):
            a.append(CrewMate())
        return a

    def createheap(self,b):
        a=b.collection
        for i in b.data:
            i.processed_time(None)
            if len(a.data)==0:
                a.insert(i)
                t1=i.arrival_time
            else:
                time=i.arrival_time-t1
                while time>0 and len(a.data)>0:
                    if a.top().ob_size()>time:
                        a.top().pt+=time
                        break
                    else:
                        a.top().completion_time=t1+a.top().ob_size()
                        time-=a.top().ob_size()
                        t1+=a.top().ob_size()
                        a.top().pt=a.top().size
                        self.completed_treasures.append(a.extract())
                t1=i.arrival_time
                a.insert(i)


    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''

        if len(self.free_crewmates)>0:
            a=self.free_crewmates.pop()
            a.data.append(treasure)
            a.load += treasure.size + treasure.arrival_time
            self.crewmates.insert(a)
        elif len(self.pseudo_free)>0:
            a=self.pseudo_free.pop()
            a.data.append(treasure)
            a.load += treasure.size + treasure.arrival_time
            self.crewmates.insert(a)
        else:
            while len(self.crewmates.data) > 0 and self.crewmates.top().load < treasure.arrival_time:
                a = self.crewmates.extract()
                a.load = 0
                self.pseudo_free.append(a)
            if len(self.pseudo_free)>0:
                a=self.pseudo_free.pop()
                a.data.append(treasure)
                a.load += treasure.size + treasure.arrival_time
                self.crewmates.insert(a)
            else:
                a=self.crewmates.extract()
                a.data.append(treasure)
                a.load+=treasure.size
                self.crewmates.insert(a)
        #print(treasure.id," inserted in ",a.f)

    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        for i in self.crewmates.data:
            self.createheap(i)
        for i in self.pseudo_free:
            self.createheap(i)
        for i in self.crewmates.data:
            t1=i.data[-1].arrival_time
            while len(i.collection.data)>0:
                a=i.collection.extract()
                a.completion_time=t1+a.ob_size()
                t1+=a.ob_size()
                self.completed_treasures.append(a)
        for i in self.pseudo_free:
            t1 = i.data[-1].arrival_time
            while len(i.collection.data) > 0:
                a = i.collection.extract()
                a.completion_time = t1 + a.ob_size()
                t1 += a.ob_size()
                self.completed_treasures.append(a)
        self.completed_treasures.sort(key=lambda obj: obj.id)
        ans=self.completed_treasures.copy()
        self.completed_treasures=[]
        return ans
