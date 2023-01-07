import pyrosim.pyrosim as pyrosim

length,width,height = 1,1,1
x,y,z = 0,0,0.5

pyrosim.Start_SDF("boxes.sdf")
for k in range(5):
    for j in range(5):
        for i in range(10):
            name = "Box" + str(i)
            pyrosim.Send_Cube(name=name, pos=[j,k,0.5+i], size=[pow(0.9,i),pow(0.9,i),pow(0.9,i)])

pyrosim.End()
