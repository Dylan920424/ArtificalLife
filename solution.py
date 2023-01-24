import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID) -> None:
        self.myId = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)*2-1
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

    def Start_Simulation(self, directOrGUI):
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myId))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myId) + ".txt"):
            time.sleep(0.01)
        fitnessFile = open("fitness" + str(self.myId) + ".txt", "r")
        self.fitness = fitnessFile.read()
        fitnessFile.close()
        # print(self.fitness)
        os.system("del fitness" + str(self.myId)+ ".txt")

    def Evaluate(self, directOrGUI):
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myId))
        while not os.path.exists("fitness" + str(self.myId) + ".txt"):
            time.sleep(0.01)
        fitnessFile = open("fitness" + str(self.myId) + ".txt", "r")
        self.fitness = fitnessFile.read()
        fitnessFile.close()
        print(self.fitness)

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)
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
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[length,width,height])
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0], size=[1,0.2,0.2])
        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0], size=[1,0.2,0.2])
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myId) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_RightLowerLeg")
        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-0.1)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-0.1)
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()
    
    def Set_ID(self, id):
        self.id = id