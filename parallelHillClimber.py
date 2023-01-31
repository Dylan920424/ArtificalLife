import solution
import constants
import copy

class PARALLEL_HILLCLIMBER:
    def __init__(self) -> None:
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(constants.populationSize):
            temp = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[i] = temp

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        for parent in self.parents:
            print("\n")
            print(self.parents[parent].fitness, self.children[parent].fitness)
            print("\n")
        self.Select()
    
    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for parent in self.parents:
            if float(self.parents[parent].fitness) > float(self.children[parent].fitness):
                self.parents[parent] = self.children[parent]

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