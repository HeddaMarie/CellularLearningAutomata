import numpy as np


# 1D CA.


#state = [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]
#new_state = [0]

#epoch = 0
#iterations = 4

#input_rules = format(22, '08b')
#print(input_rules)

# you, and your neighbour count as neighbourhood, if 0 and neighbour == 1.

rule1 = [0, 0, 0]  # center dead
rule2 = [0, 0, 1]  # center alive
rule3 = [0, 1, 0]  # center alive
rule4 = [0, 1, 1]  # center alive
rule5 = [1, 0, 0]  # center dead
rule6 = [1, 0, 1]  # center alive
rule7 = [1, 1, 0]  # center alive
rule8 = [1, 1, 1]  # center dead
#3 dead cases. rest alive.


class CA:
    def __init__(self, state, rule, iterations):
        self.state = state
        self.rule = rule
        self.binary_rules = format(self.rule, '08b')
        self.iterations = iterations
        #self.generations = np.array(self.run_num_iterations(state, iterations))
        #self.generations = []

    def next_round(self, state):
        next_round = [0] * len(self.state)

        for i in range(len(self.state)):
            left = self.state[i-1]
            center = self.state[i]
            right = self.state[(i+1) % len(self.state)]
            next_round[i] = self.rules(left, center, right)
        self.state = next_round
        return self.state

    #00010110
    def rules(self, left, center, right):

        if (left == 0 and center == 0 and right == 0): return int(self.binary_rules[7])  # rule 1
        if (left == 0 and center == 0 and right == 1): return int(self.binary_rules[6])  # rule 2
        if (left == 0 and center == 1 and right == 0): return int(self.binary_rules[5])  # rule 3
        if (left == 0 and center == 1 and right == 1): return int(self.binary_rules[4])  # rule 4
        if (left == 1 and center == 0 and right == 0): return int(self.binary_rules[3])  # rule 5
        if (left == 1 and center == 0 and right == 1): return int(self.binary_rules[2])  # rule 6
        if (left == 1 and center == 1 and right == 0): return int(self.binary_rules[1])  # rule 7
        if (left == 1 and center == 1 and right == 1): return int(self.binary_rules[0])  # rule 8

    def run_num_iterations(self, state, iterations):
        result = [state] 
        for i in range(iterations):
            next_run = self.next_round(state) #store the return from next_round to pass as param for run_num_iterations
            state = next_run
            result.append(state)
        format_result = np.array(result)
        return format_result
