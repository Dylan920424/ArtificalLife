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
    box = [0,0,1]
    length,width,height = random.random(), random.random(), random.random()
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="link0", pos=box, size=[length,width,height])
    boxes = [box]
    sizes = [[length,width,height]]
    axises = ["0 0 1", "0 1 0", "1 0 0"]
    for i in range(1, links):
        connect = random.randint(0,i-1)
        direction,axis = random.randint(0,2), random.randint(0,2)
        posneg = random.randint(0,1)
        chosen = [-sizes[connect][0]/2, sizes[connect][0]/2, -sizes[connect][1]/2, sizes[connect][1]/2, -sizes[connect][2]/2, sizes[connect][2]/2]
        pos = [boxes[connect][0]+(random.random()-0.5)*sizes[connect][0],boxes[connect][1]+(random.random()-0.5)*sizes[connect][1],boxes[connect][2]+(random.random()-0.5)*sizes[connect][2]]
        pos[direction] = boxes[connect][direction] + chosen[direction*2+posneg]
        joints.append("link"+str(connect)+"_link"+str(i))
        pyrosim.Send_Joint(name = "link"+str(connect)+"_link"+str(i), parent="link"+str(connect), child="link"+str(i), type="revolute", position=pos, jointAxis=axises[axis])
        length,width,height = random.random(), random.random(), random.random()
        sizes.append([length,width,height])
        box = [(random.random()-0.5)*length, (random.random()-0.5)*width, (random.random()-0.5)*height]
        chosen = [-length/2, length/2, -width/2, width/2, -height/2, height/2]
        box[direction] = chosen[direction*2+posneg]
        boxes.append(box)
        pyrosim.Send_Cube(name="link"+str(i), pos=box, size=[length,width,height])
    print(boxes, sizes)
    pyrosim.End()

def Generate_Brain(links):
    pyrosim.Start_NeuralNetwork("brain.nndf")
    sensor = 0
    for link in range(links):
        if random.random() >= 0.2:
            pyrosim.Send_Sensor_Neuron(name=sensor, linkName="link"+str(link))
            sensor += 1
    motor = sensor
    for joint in joints:
        if random.random() >= 0.2:
            pyrosim.Send_Motor_Neuron(name=motor, jointName=joint)
            motor += 1
    for sensor in range(sensor):
        for motor in range(sensor,motor):
            pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=motor, weight=random.random()*2-1)
    pyrosim.End()

links = random.randint(2, c.maxLinks)
joints = []
Create_World()
Generate_Body(links)
Generate_Brain(links)