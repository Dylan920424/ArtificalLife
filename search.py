import os
import parallelHillClimber
import multiHillClimber
import matplotlib.pyplot as plt
import numpy as np

# os.system("del brain*.nndf")
# os.system("del body*.urdf")
# os.system("del fitness*.txt")
# phc = parallelHillClimber.PARALLEL_HILLCLIMBER()
# tmp = np.absolute(np.array(phc.Evolve()))
# phc.Show_Best()
# plt.plot(tmp)
# plt.show()

# for i in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")

# For plotting the fitness curves
if __name__ == '__main__':
    import time
    start_time = time.time()
    for i in range(5):
        os.system("del brain*.nndf")
        os.system("del body*.urdf")
        os.system("del fitness*.txt")
        # phc = parallelHillClimber.PARALLEL_HILLCLIMBER()
        phc = multiHillClimber.PARALLEL_HILLCLIMBER()
        temp1, temp2, temp3 = np.absolute(np.array(phc.Evolve()))
        # phc.Show_Best()
        plt.subplot(121)
        plt.plot(temp1)
        plt.subplot(122)
        plt.plot(temp2, "r")
        plt.plot(temp3, "b")
    print("--- %s seconds ---" % (time.time() - start_time))

plt.show()