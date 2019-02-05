import numpy as np
from Markov import Markov_process
np.random.seed(101)

class rth_success(Markov_process):
    """
    example for p = .2
    Q = np.array([
            [.8,.2,.0], 
            [.0,.8,.2], 
            [.0,.0,1.]])
    """
    def __init__(self, r, p):
        states = list(range(r+1))
        Q = np.zeros((r+1, r+1))
        # fail and I'm still in this state
        np.fill_diagonal(Q, 1-p)
        # successes take me to the next state
        np.fill_diagonal(Q[:-1, 1:], p)
        Q[-1,-1] = 1
        print(Q)
        accept_states = (states[-1],)
        Markov_process.__init__(self, states, Q, accept_states)

if __name__ == "__main__":
    game = rth_success(5, .6)
    print(game.sample_game())
    print(game.sample_game())
    print(game.sample_game(stop=20))
    # print(game.sim_avg(n=1000))
