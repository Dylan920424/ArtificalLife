import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import numpy
from itertools import groupby
import time

class ROBOT:
    def __init__(self, solutionID, tmp=False) -> None:
        self.myID = solutionID
        self.robotId = p.loadURDF("body" + str(self.myID) + ".urdf")
        self.nn = NEURAL_NETWORK("brain" + str(self.myID) + ".nndf")
        os.system("del brain" + str(self.myID) + ".nndf")
        os.system("del body" + str(self.myID)+ ".urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,i):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(i)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
    
    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = basePosition[0]
        # s = numpy.zeros(c.steps)
        # for sensor in self.sensors:
        #     # s += numpy.mean(self.sensors[sensor].Get_List())
        #     s += self.sensors[sensor].Get_List()
        # s = max(sum(g)/-7 for k, g in groupby(s) if k == -7)
        f = open("tmp" + str(self.myID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        # f.write(str(s))
        f.close()
        os.system("ren tmp"+str(self.myID)+".txt " + "fitness"+str(self.myID)+".txt")