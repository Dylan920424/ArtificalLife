import numpy

amplitudeF, frequencyF, phaseOffsetF = numpy.pi/4, 10, 0
amplitudeB, frequencyB, phaseOffsetB = numpy.pi/4, 10, numpy.pi/2

steps = 1000
maxForce = 500
sleepTime = 1/48000

numberOfGenerations = 1
populationSize = 1

numSensorNeurons = 4
numMotorNeurons = 8
motorJointRange = 0.5