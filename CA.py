import numpy as np


class CA:
    def __init__(self, state, rule, iterations):
        self.state = state
        self.rule = rule
        self.binary_rules = format(self.rule, '08b')
        self.iterations = iterations


    def next_round(self, state):
        next_round = [0] * len(self.state)

        for i in range(len(self.state)):
            left = self.state[i-1]
            center = self.state[i]
            right = self.state[(i+1) % len(self.state)]
            next_round[i] = self.rules(left, center, right)
        self.state = next_round
        return self.state


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
            next_run = self.next_round(state)
            state = next_run
            result.append(state)
        format_result = np.array(result)
        return format_result
