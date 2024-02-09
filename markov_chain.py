'''
MarkovChain class. Instance of this class represents a Discrete-time Markov chain.
A Markov Chain consists of different states that are connected to each other.
'''

class MarkovChain:
    def __init__(self, name, S):
        self.__name = name
        self.__S = S  # state space is a list of State objects

    def size(self):
        '''Returns size of the state space S'''
        return len(self.__S)

    def __str__(self):
        string = f"Name: {self.__name}\n"
        for state in self.__S:
            string += str(state) + "\n"
        return string.strip()
