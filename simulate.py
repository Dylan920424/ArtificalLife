import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c
import sys
from simulation import SIMULATION
import os

os.system("python generate.py")
directOrGUI = "GUI"
simulation = SIMULATION(directOrGUI, "")
simulation.Run()
simulation.Get_Fitness()