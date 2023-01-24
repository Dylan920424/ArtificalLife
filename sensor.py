import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName) -> None:
        self.linkName = linkName
        self.values = numpy.zeros(c.steps)

    def Get_Value(self,i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Get_List(self):
        return self.values

    def Save_Values(self):
        numpy.save('data/'+self.linkName+'.npy', self.values)