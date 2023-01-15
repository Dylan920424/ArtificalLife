import pyrosim.pyrosim as pyrosim
import constants as c
import numpy
import pybullet as p

class MOTOR:
    def __init__(self,jointName) -> None:
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if self.jointName == "Torso_FrontLeg":
            self.amplitude, self.frequency, self.offset = c.amplitudeB, c.frequencyB, c.phaseOffsetB
        else:
            self.amplitude, self.frequency, self.offset = c.amplitudeB, c.frequencyB/2, c.phaseOffsetB
        self.motorValues = numpy.sin(numpy.linspace(0,numpy.pi*2,c.steps)*self.frequency+self.offset)*self.amplitude

    def Set_Value(self, robotId,i):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=self.jointName, controlMode=p.POSITION_CONTROL, targetPosition=self.motorValues[i], maxForce=c.maxForce)

    def Save_Values(self):
        numpy.save('data/'+self.jointName+'.npy', self.motorValues)