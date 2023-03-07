import solution
import constants
import copy
import os
from operator import itemgetter
import multiprocessing
import math

class PARALLEL_HILLCLIMBER:
    def __init__(self) -> None:
        self.parents = {}
        self.nextAvailableID = 0
        self.fitness_curve = []
        self.morpho_curve = []
        self.brain_curve = []
        for i in range(constants.populationSize):
            temp = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[i] = temp

    def Evolve(self):
        self.Evaluate(self.parents)
        fitness, morpho, brain = self.Find_Best()
        self.fitness_curve.append(fitness)
        self.morpho_curve.append(morpho)
        self.brain_curve.append(brain)
        last = fitness
        gens = 0
        limit = math.floor(math.log2(constants.populationSize))
        for switch in range(limit):
            gens = 0
            while True:
                self.Evolve_For_One_Generation(switch%2)
                fitness, morpho, brain = self.Find_Best()
                self.fitness_curve.append(fitness)
                self.morpho_curve.append(morpho)
                self.brain_curve.append(brain)
                if fitness == last:
                    gens += 1
                last = fitness
                if gens == constants.numberOfStagnation:
                    break
                if self.nextAvailableID >= constants.maxGen:
                    break
            if self.nextAvailableID >= constants.maxGen:
                    break
            self.Catastrophe()
        return self.fitness_curve, self.morpho_curve, self.brain_curve

    def Evolve_For_One_Generation(self, version):
        self.Spawn()
        self.Mutate(version)
        self.Evaluate(self.children)
        # for parent in self.parents:
        #     print("\n")
        #     print(self.parents[parent].fitness, self.children[parent].fitness)
        #     print("\n")
        self.Select()
    
    def Catastrophe(self):
        fitnesses = [(i, float(self.parents[i].fitness)) for i in self.parents]
        fitnesses = sorted(fitnesses, key=itemgetter(1))
        # print(fitnesses)
        rankings = [i[0] for i in fitnesses]
        best = 0
        worst = len(rankings)-1
        while best < worst:
            self.parents[rankings[worst]] = copy.deepcopy(self.parents[rankings[best]])
            self.parents[rankings[worst]].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            best += 1
            worst -= 1
        
    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self, version):
        for child in self.children:
            self.children[child].Mutate_mhc(version)
            # self.children[child].Mutate()

    def Select(self):
        for parent in self.parents:
            if float(self.parents[parent].fitness) > float(self.children[parent].fitness):
                self.parents[parent] = self.children[parent]

    def Find_Best(self):
        min = float(self.parents[0].fitness)
        morpho = 0
        brain = 0
        for parent in self.parents:
            morpho += int(self.parents[parent].morpho)
            brain += int(self.parents[parent].brain)
            if float(self.parents[parent].fitness) < min:
                min = float(self.parents[parent].fitness)
        return min, morpho/len(self.parents), brain/len(self.parents)

    def Show_Best(self):
        min = float(self.parents[0].fitness)
        show = self.parents[0]
        for parent in self.parents:
            if float(self.parents[parent].fitness) < min:
                min = float(self.parents[parent].fitness)
                show = self.parents[parent]
        print(min)
        show.Start_Simulation("GUI")

        # max = float(self.parents[0].fitness)
        # show = self.parents[0]
        # for parent in self.parents:
        #     if float(self.parents[parent].fitness) > max:
        #         max = float(self.parents[parent].fitness)
        #         show = self.parents[parent]
        # print(max)
        # show.Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for parent in solutions:
            solutions[parent].Start_Simulation("DIRECT")
        for parent in solutions:
            solutions[parent].Wait_For_Simulation_To_End()