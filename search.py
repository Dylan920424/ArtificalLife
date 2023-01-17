import os
import hillclimber

hc = hillclimber.HILLCLIMBER()
hc.Evolve()
hc.Show_Best()

# for i in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")