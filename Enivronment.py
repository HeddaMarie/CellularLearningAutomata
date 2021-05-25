import numpy as np
import pandas as pd
import math
from random import random, seed
import uuid
import datetime

class Environment:

    def __init__(self, chance):
        self.chance = chance
        self.id = uuid.uuid4()

        self.prob = 0
        self.random = round(random() * 1)

    def probability(self, state):
        #pull in the current state/generation.
        live = 0
        dead = 0

        #count the living and dead cells in a loop and stor them.
        for i in state:
            if i == 1:
                live += 1
            elif i == 0:
                dead += 1

        livepercentage = (live / len(state))
        deadpercentage = (dead / len(state)) #in case we had any use for it.

        total = live + dead

        if 0.4 <= livepercentage <= 0.6:
            self.prob = livepercentage
        else:
            self.prob = livepercentage

    def cast_die(self, current_state):
        result = np.random.rand()
        chance = self.chance
        if chance != 0:  # for the very small chance that result is 0.
            if result <= chance:
                return not current_state
            else:
                return current_state
        else:
            return current_state

    def gaussian(self, x, mu=0.5, sig=0.1):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


    def gaussEval(self, randnum, envprob):
        if randnum <= self.gaussian(envprob):
            return True
        else:
            return False

    def decide(self):

        if 0.40 <= self.prob <= 0.6:
            return self.cast_die(True)
        else:
            return self.cast_die(False)
