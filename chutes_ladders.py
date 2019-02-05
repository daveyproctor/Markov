import numpy as np
from Markov import Markov_process
np.random.seed(100)

if __name__ == "__main__":
    """ Results from a simple chutes and ladders game """
    a = .5
    Q = np.array((0,0,a,a,0,a,0,0,0,0,a,a,0,0,0,0,a,a,0,0,0,0,0,a,1)).reshape(5,5).T
    states = np.array([1,3,4,7,9])
    accept_states = (9,)
    game = Markov_process(states, Q, accept_states)

    s = np.array([1,0,0,0,0])
    print(game.median_duration(s))
    # classes vs instances:
    print(game.sample_game())
    asdf
    print(Markov_process.sample_game(game))

    print(game.sim_median())
    print(game.sim_avg())



"""
    # relatedly, the CDF of the duration is F(x=n) = Q^n_{0,accept_state}
    print(np.linalg.matrix_power(Q,7)[0,accept_state])

def median_duration(s, Q, accept_state):
    ""Stops once we are >1/2 likely to be in the accept state""
    for i in itertools.count():
        if s[accept_state] > .5:
            print("median state: {}, num_steps: {}".format(s,i))
            return i
        print(s)
        s = np.dot(s, Q)


def sim_median(s,Q,accept_state,n=100,printing=False):
    "" Numerical simulation of the median duration
    runs many games and determines median game length ""
    games = np.array([len(sample_game(s,Q,(accept_state,))) for i in range(n)])
    if printing:
        print(games)
    games = np.sort(games)
    return np.median(games)


def sim_avg(s,Q,accept_state,n=100,printing=False):
    "" Numerical simulation of the avg duration
    runs many games and determines avg game length ""
    games = np.array([len(sample_game(s,Q,(accept_state,))) for i in range(n)])
    if printing:
        print(games)
    return np.mean(games)
"""

