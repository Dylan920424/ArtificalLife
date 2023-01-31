import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID) -> None:
        self.myId = nextAvailableID
        self.links = random.randint(2, c.maxLinks)
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
        self.Create_World()
        if random.random() > 0.05 and len(self.have_sensor) > 0 and len(self.have_motors) > 0:
            if len(self.have_sensor) == 1: 
                randomRow = 0
            else:
                randomRow = random.randint(0, len(self.have_sensor)-1)
            if len(self.have_motors) == 1:
                randomColumn = 0
            else:
                randomColumn = random.randint(0, len(self.have_motors)-1)
            self.weights[randomRow, randomColumn] = random.random()*2-1
        # else:
        #     self.Create_Body()
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
        box = [0,0,1]
        length,width,height = random.random(), random.random(), random.random()
        pyrosim.Start_URDF("body" + str(self.myId) + ".urdf")
        pyrosim.Send_Cube(name="link0", pos=box, size=[length,width,height])
        boxes = [box]
        sizes = [[length,width,height]]
        axises = ["0 0 1", "0 1 0", "1 0 0"]
        self.have_sensor = []
        self.have_motors = []
        for i in range(1, self.links):
            connect = random.randint(0,i-1)
            direction,axis = random.randint(0,2), random.randint(0,2)
            posneg = random.randint(0,1)
            chosen = [-sizes[connect][0]/2, sizes[connect][0]/2, -sizes[connect][1]/2, sizes[connect][1]/2, sizes[connect][2]/2, sizes[connect][2]/2]
            pos = [boxes[connect][0]+(random.random()-0.5)*sizes[connect][0],boxes[connect][1]+(random.random()-0.5)*sizes[connect][1],boxes[connect][2]+(random.random()-0.5)*sizes[connect][2]]
            pos[direction] = boxes[connect][direction] + chosen[direction*2+posneg]
            if random.random() > 0.2: self.have_motors.append("link"+str(connect)+"_link"+str(i))
            pyrosim.Send_Joint(name = "link"+str(connect)+"_link"+str(i), parent="link"+str(connect), child="link"+str(i), type="revolute", position=pos, jointAxis=axises[axis])
            length,width,height = random.random(), random.random(), random.random()
            sizes.append([length,width,height])
            box = [(random.random()-0.5)*length, (random.random()-0.5)*width, (random.random()-0.5)*height]
            chosen = [-length/2, length/2, -width/2, width/2, height/2, height/2]
            box[direction] = chosen[direction*2+posneg]
            boxes.append(box)
            if random.random() >= 0.2:
                pyrosim.Send_Cube(name="link"+str(i), pos=box, size=[length,width,height], color="0.0 1.0 0.0 1.0", colorname="Green")
                self.have_sensor.append(i)
            else:
                pyrosim.Send_Cube(name="link"+str(i), pos=box, size=[length,width,height])
        self.weights = numpy.random.rand(len(self.have_sensor),len(self.have_motors))*2-1
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myId) + ".nndf")
        self.sensors = 0
        for link in self.have_sensor:
            pyrosim.Send_Sensor_Neuron(name=self.sensors, linkName="link"+str(link))
            self.sensors += 1
        self.motors = self.sensors
        for joint in self.have_motors:
            pyrosim.Send_Motor_Neuron(name=self.motors, jointName=joint)
            self.motors += 1
        for sensor in range(self.sensors):
            for motor in range(self.sensors,self.motors):
                pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=motor, weight=self.weights[sensor][motor-len(self.have_sensor)])
        pyrosim.End()
        
    def Set_ID(self, id):
        self.id = id