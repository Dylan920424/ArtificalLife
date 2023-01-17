import numpy
import pyrosim.pyrosim as pyrosim
import os
import random

class SOLUTION:
    def __init__(self) -> None:
        self.weights = numpy.random.rand(3,2)*2-1
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

    def Evaluate(self, directOrGUI):
        os.system("python simulate.py " + directOrGUI)
        fitnessFile = open("fitness.txt", "r")
        self.fitness = fitnessFile.read()
        fitnessFile.close()

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow, randomColumn] = random.random()*2-1
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

    def Create_World(self):
        length,width,height = 1,1,1
        x,y,z = 2,2,0.5

        pyrosim.Start_SDF("world.sdf")
        # for k in range(5):
        #     for j in range(5):
        #         for i in range(10):
        #             name = "Box" + str(i)
        #             pyrosim.Send_Cube(name=name, pos=[j,k,0.5+i], size=[pow(0.9,i),pow(0.9,i),pow(0.9,i)])
        pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])

        pyrosim.End()

    def Create_Body(self):
        length,width,height = 1,1,1
        x,y,z = 1.5,0,1.5
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length,width,height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-0.1)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-0.1)
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()