import numpy as np
import uuid
from Enivronment import Environment as Env



class Automaton:

    def __init__(self, num_states, rules):
        self.num_states = num_states
        self.state = np.random.randint(2 * num_states)+1
        self.rewards = 0
        self.punishments = 0 
        self.id = uuid.uuid4()
        self.left_arm = 0 
        self.right_arm = 0 
        self.rules = [rules]
        self.active = 0

    def reward(self):

        if (self.state <= self.num_states) and (self.state > 1):
            self.left_arm += 1
            self.state = self.state - 1
            self.rewards += 1


        elif (self.state > self.num_states) and (self.state < 2 * self.num_states):
            self.right_arm += 1
            self.state = self.state + 1
            self.rewards += 1


        else:
            if self.state == 1:
                self.left_arm +=1
            elif self.state == 6:
                self.right_arm +=1
        self.rewards += 1

        return self.state

    def punish(self):
        if self.state <= self.num_states:
            self.right_arm += 1
            self.state = self.state + 1
            self.punishments += 1
            return self.state

        elif self.state > self.num_states:
            self.right_arm += 1
            self.state = self.state - 1
            self.punishments += 1
            return self.state

    def evaluateArm(self):
        if self.state > self.num_states:
            return 1
        else:
            return 0