import numpy as np
import itertools

class Markov_process(object):
    """Implements a Markov chain / process.
    Each state succeeds from the last according to Q,
    the state transition matrix"""

    def __init__(self, states, Q, accept_states=()):
        """ assumes ordering on states and Q rows is the same.
        No accept_states by default"""
        self.named_states = np.array(states)
        self.Q = Q
        # need the indices
        self.accept_states = np.array([i for i,s in enumerate(states) if s in accept_states], dtype=int)

    def sample_game(self, s=None, stop=5):
        """Starting from distribution s (state 0 by default)
        simulates a game till accept state.
        returns array of each named state visited"""
        states = []
        if s is None:
            state = 0
        else:
            state = np.random.choice(range(len(s)), p=s)
        if stop is None:
            it = itertools.count()
        else:
            it = range(stop)
        for i in it:
            states.append(state)
            if state in self.accept_states:
                break
            row = self.Q[state]
            # where to next?
            state = np.random.choice(range(len(row)), p=row)
        states = np.array(states, dtype=int)
        return self.named_states[states]
    
    def sim_distribution(self, stop=10):
        print(self.named_states)
        n = len(self.named_states)
        s=np.ones((n))/n,
        print(s)
        for i in range(stop):
            s = np.dot(s, self.Q)
            print(s)
        return

    def median_duration(self, s):
        """Starting from distribution s,
        Stops once we are >1/2 likely to be in an accept state"""
        for i in itertools.count():
            if max(s[self.accept_states]) > .5:
                return i
            s = np.dot(s, self.Q)

    def sim_median(self, s=None, n=100):
        """ Numerical simulation of the median duration
        runs many games and determines median game length """
        # first state does not count towards move length
        games = np.array([len(self.sample_game(s))-1 for i in range(n)])
        return np.median(games)

    def sim_avg(self, s=None, n=100):
        """ Numerical simulation of the avg duration
        runs many games and determines avg game length """
        games = np.array([len(self.sample_game(s))-1 for i in range(n)])
        return np.mean(games)




"""
                print(states)
                print(self.named_states)
                print(self.named_states[[0,1,1,1,2]])
                print(self.named_states[states])
            # print(state)
            # print(self.Q.shape)
            # print(row.shape)
            print(self.Q)
            print(self.Q.shape)
            print(self.Q[0])
"""
