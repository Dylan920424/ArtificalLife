import pyrosim.pyrosim as pyrosim
import random
import constants as c

def Create_World():
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

def Generate_Body(links):
    x,y,z = 0,0,1
    length,width,height = random.random(), random.random(), random.random()*0.5
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="link0", pos=[x, y, z], size=[length,width,height])
    for i in range(1, links):
        if i == 1:
            pyrosim.Send_Joint(name = "link"+str(i-1)+"_link"+str(i), parent="link"+str(i-1), child="link"+str(i), type="revolute", position=[-length/2,y,z], jointAxis="0 0 1")
        else:
            pyrosim.Send_Joint(name = "link"+str(i-1)+"_link"+str(i), parent="link"+str(i-1), child="link"+str(i), type="revolute", position=[-length,0,0], jointAxis="0 0 1")
        length,width,height = random.random(), random.random(), random.random()*0.5
        pyrosim.Send_Cube(name="link"+str(i), pos=[-length/2, 0, 0], size=[length,width,height])
    # pyrosim.Send_Cube(name="Torso", pos=[x,y,z], size=[length,width,height])
    # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    # pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length,width,height])
    # pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    # pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length,width,height])
    pyrosim.End()

def Generate_Brain(links):
    pyrosim.Start_NeuralNetwork("brain.nndf")
    # pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    # pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    # pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    # pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    # pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-0.1)
    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-0.1)
    sensor = 0
    for link in range(links):
        if random.random() >= 0.2:
            pyrosim.Send_Sensor_Neuron(name=sensor, linkName="link"+str(link))
            sensor += 1
    motor = sensor
    for link in range(1, links):
        if random.random() >= 0.2:
            pyrosim.Send_Motor_Neuron(name=motor, jointName="link"+str(link-1)+"_link"+str(link))
            motor += 1
    for sensor in range(sensor):
        for motor in range(sensor,motor):
            pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=motor, weight=random.random()*2-1)
    pyrosim.End()

links = random.randint(2,c.maxLinks)
Create_World()
Generate_Body(links)
Generate_Brain(links)