'''
    Python file to implement the class CrewMate
'''
from heap import Heap,comp2
class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        self.load=0
        # Write your code here
        self.collection=Heap(comp2,[])
        self.data=[]

    
    # Add more methods if required