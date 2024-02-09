'''
State class. A Markov Chain consists of states.
Every state has an ID (str) and connections to other states (and/or itself).
The connections are equipped with a probability; how probable is it to transition from state A to state B in the next step.
'''

class State:
    def __init__(self, id):
        self.__id = id
        self.__connections = {}    # dictionary contains the state's connections and 
                                          # their probabilities, P(self-loop)=0 by default
    def createConnection(self, state, P):
        '''Creates a connection to another state. Function overwrites an existing connection with a new P'''
        self.__connections[state] = P

    def getConnections(self):
        return self.__connections

    def __str__(self):
        desc = f"ID: {self.__id}\n"
        # TODO
