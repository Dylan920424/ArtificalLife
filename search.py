import os
import parallelHillClimber

os.system("del brain*.nndf")
os.system("del body*.urdf")
os.system("del fitness*.txt")
phc = parallelHillClimber.PARALLEL_HILLCLIMBER()
phc.Evolve()
phc.Show_Best()

# for i in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")