from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import constants as c
import pyrosim.pyrosim as pyrosim

class SIMULATION:
    def __init__(self) -> None:
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
    
    def Run(self):
        for i in range(c.steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesB[i], maxForce=c.maxForce)
            # pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesF[i], maxForce=c.maxForce)
            time.sleep(c.sleepTime)

    def __del__(self):
        p.disconnect()