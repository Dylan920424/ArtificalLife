import os
import parallelHillClimber
import matplotlib.pyplot as plt
import numpy as np

os.system("del brain*.nndf")
os.system("del body*.urdf")
os.system("del fitness*.txt")
phc = parallelHillClimber.PARALLEL_HILLCLIMBER()
phc.Evolve()
phc.Show_Best()

# for i in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")

# For plotting the fitness curves
# for i in range(5):
#     os.system("del brain*.nndf")
#     os.system("del body*.urdf")
#     os.system("del fitness*.txt")
#     phc = parallelHillClimber.PARALLEL_HILLCLIMBER()
#     temp = np.absolute(np.array(phc.Evolve()))
#     plt.plot(temp)

# plt.show()