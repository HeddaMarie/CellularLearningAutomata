from Automaton import Automaton
import numpy as np
import matplotlib.pyplot as plt
from random import random
from Enivronment import Environment as Env
import time
import datetime as dt
import pathlib
import sys
sys.path.append('../LA')
sys.path.append('../CA')

class CLA:
    def __init__(self, num_states, state, rule, iterations, experimentname, experimentnr, experimentdato, envchance=0, has_damage=False, gaussian=False):
        self.start_time = time.time()
        self.chance = envchance
        self.experimentname = experimentname
        self.experimentnr = experimentnr
        self.experimentdate = experimentdato
        self.gaussian = gaussian
        self.has_damage = has_damage
        self.rule_present = []
        self.num_states = num_states  # passed to the TA.
        self.state = state
        self.rule = rule
        self.binary_rules = format(self.rule, '08b')
        # self.results = open('results.txt', 'a')
        self.iterations = iterations
        self.La_list = self.createLA()
        self.environments = self.createENV()
        self.generations = np.array(self.run_num_iterations(state, iterations))



    def prepare_csv(self, resultline):
        experimentnr = self.experimentnr
        name = self.experimentname
        dato = self.experimentdate
        pathlib.Path(f'./results/{experimentnr}').mkdir(parents=True, exist_ok=True)
        results = f'./results/{experimentnr}/{name}-{dato}.csv'
        if resultline == "":
            with open(results, 'w') as f:
                headers = "LA.state ;CA.state;Env probability; T(iteration)"
                f.write(headers)
        elif resultline != "":
            with open(results, 'a') as fw:
                fw.writelines(resultline)

    def next_round(self, state):
        next_round = [0] * len(self.state)

        for i in range(len(self.state)):
            left = self.state[i - 1]
            center = self.state[i]
            right = self.state[(i + 1) % len(self.state)]
            next_round[i] = self.TA_learn(left, center, right)
        self.state = next_round
        return self.state

    def next_round_damaged(self, state, damaged_indices=list(range(100))):
        next_round = [0] * len(self.state)
        #print(f'damanged cells: {damaged_indices}')
        for i in range(len(self.state)):
            left = self.state[i - 1]
            center = self.state[i]
            right = self.state[(i + 1) % len(self.state)]
            # next_round[i] = self.rules(left, center, right)
            next_round[i] = self.TA_learn(left, center, right)
            if i in damaged_indices:
                #print(damaged_indices)
                next_round[i] = 0
        self.state = next_round
        return self.state

    # Creates all the LA's the class needs and stores them in the self.La_list class variable as a list.
    def createLA(self):
        regler = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]])

        list_of_la = []
        for cell in range(8):
            TA = Automaton(self.num_states, regler[cell])
            # For each TA we attach 8 rules.
            # print(TA.rules,"\n")
            # print("ID:\t",TA.id)
            list_of_la.append(TA)
        return list_of_la

    # Creates a list of environments. Stores them in the self.environment list if needed.
    def createENV(self):
        liste = self.La_list
        envlist = []
        for TA in liste:
            environment = Env(self.chance)
            envlist.append(environment)
        return envlist

    # This method runs through all the neighbourhoods, matches LA's with a corresponding environment.
    # The method sets the active variable in the LA class to 1 if the neighbourhood is identified during the run.
    # This is set back to 0 by the update_la() methods when the update_la() is run at the end of the CA update.

    def TA_learn(self, left, center, right):

        # Create local learning by pulling the cells position in the array in from next_round(), and call LA[i] for first LA in row, and la[i+1] for next.
        # Store each Set of LAs in a long array that are offset by 7 (0(i) to 7(i+7)). This should allow for local learning.
        # pull the position from next_run() by getting the cells position.
        eval_this = [left, center, right]
        neighbourhood = "".join(str(e) for e in eval_this)
        if neighbourhood == '111':
            self.rule_present.append(0)
            TA = self.La_list[0]
            env = self.environments[0]
            env.right_arm = TA.right_arm
            env.left_arm = TA.left_arm
            TA.active = 1

            return TA.evaluateArm()

        elif neighbourhood == '110':
            self.rule_present.append(1)
            TA = self.La_list[1]
            env = self.environments[0]
            env.right_arm = TA.right_arm
            env.left_arm = TA.left_arm
            TA.active = 1

            return TA.evaluateArm()

        elif neighbourhood == '101':
            self.rule_present.append(2)
            TA = self.La_list[2]
            env = self.environments[0]
            env.right_arm = TA.right_arm
            env.left_arm = TA.left_arm
            TA.active = 1

            return TA.evaluateArm()

        elif neighbourhood == '100':
            self.rule_present.append(3)
            TA = self.La_list[3]
            env = self.environments[0]
            env.right_arm = TA.right_arm
            env.left_arm = TA.left_arm
            TA.active = 1

            return TA.evaluateArm()

        elif neighbourhood == '011':
            self.rule_present.append(4)
            TA = self.La_list[4]
            env = self.environments[0]
            env.right_arm = TA.right_arm
            env.left_arm = TA.left_arm
            TA.active = 1

            return TA.evaluateArm()

        elif neighbourhood == '010':
            self.rule_present.append(5)
            TA = self.La_list[5]
            env = self.environments[0]
            env.right_arm = TA.right_arm
            env.left_arm = TA.left_arm
            TA.active = 1

            return TA.evaluateArm()

        elif neighbourhood == '001':
            self.rule_present.append(6)
            TA = self.La_list[6]
            env = self.environments[0]
            env.right_arm = TA.right_arm
            env.left_arm = TA.left_arm
            TA.active = 1

            return TA.evaluateArm()

        elif neighbourhood == '000':
            self.rule_present.append(7)
            TA = self.La_list[7]
            env = self.environments[0]
            env.right_arm = TA.right_arm
            env.left_arm = TA.left_arm
            TA.active = 1

            return TA.evaluateArm()

    # ONLY for One dimensional deterministic CA production.
    def rules(self, left, center, right):

        if (left == 0 and center == 0 and right == 0): return int(self.binary_rules[7])  # rule 1
        if (left == 0 and center == 0 and right == 1): return int(self.binary_rules[6])  # rule 2
        if (left == 0 and center == 1 and right == 0): return int(self.binary_rules[5])  # rule 3
        if (left == 0 and center == 1 and right == 1): return int(self.binary_rules[4])  # rule 4
        if (left == 1 and center == 0 and right == 0): return int(self.binary_rules[3])  # rule 5
        if (left == 1 and center == 0 and right == 1): return int(self.binary_rules[2])  # rule 6
        if (left == 1 and center == 1 and right == 0): return int(self.binary_rules[1])  # rule 7
        if (left == 1 and center == 1 and right == 1): return int(self.binary_rules[0])  # rule 8

    # This functions runs once the entire CA generation has been matched against the LA with corresponding neighbourhood, and evaluated based on the current state of that LA with LA.evaluate_arm()
    # LA's that have neighbourhoods that was recognized during this round have the active variable set to 1. This is reset during the update so that we only ever update the active LA.
    def update_la(self):
        env = self.environments[0]
        for n in range(8):
            TA = self.La_list[n]
            # print("Rule:", TA.rules)
            if TA.active == 1:
                if env.decide():
                    TA.reward()
                    TA.active = 0
                else:
                    TA.punish()
                    TA.active = 0

    def update_la_gaussian(self):
        env = self.environments[0]
        randnum = np.random.rand() 
        for n in range(8):
            TA = self.La_list[n]
            if TA.active == 1:
                if env.gaussEval(randnum, env.prob):
                    TA.reward()
                    TA.active = 0
                else:
                    TA.punish()
                    TA.active = 0

    def store_la_state(self):
        la_state = []
        for i in range(len(self.La_list)):
            new_state = self.La_list[i].state
            la_state.append(new_state)
        la_state_result = np.array(la_state)
        return la_state


    # This runs the entire class, and calls every other method needed to run.
    #headers = "LA.state ,CA.state, Env probability, LA rewards, LA punishments, T(Iteration)"

    def run_num_iterations(self, state, iterations):
        self.prepare_csv("") #Print the headers
        #print(self.store_la_state())

        damaged_cell_indices = np.random.choice(np.arange(1000), 100, replace=False) # Must be kept static for all iterations.
        result = [state]
        for i in range(iterations):
            env = self.environments[0]
            self.store_la_state()
            csv_la_state = self.store_la_state()
            csv_state = str(state)
            csv_state_formatted = str(csv_state).replace('\n', '').replace(',', '').replace(' ', ', ')
            env.probability(state)
            csv_prob = env.prob
            self.prepare_csv("\n"+str(csv_la_state) + ";" +str(csv_state_formatted)+";"+str(csv_prob) + ";" +str(i))

            if self.has_damage and i > 499:
                next_run = self.next_round_damaged(state, damaged_cell_indices)
            else:
                next_run = self.next_round(state)

            if self.gaussian:
                self.update_la_gaussian()
            else:
                self.update_la()

            state = next_run
            result.append(state)
        format_result = np.array(result)
        finaltime = time.time() - self.start_time
        print(finaltime)
        return format_result
