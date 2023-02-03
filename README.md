# ArtificalLife
run the search.py file to run parallel hill climber evolution with both body and brain mutations training the body to move away from the camera

# Constants that could be changed in constants.py
- numberOfGenerations: The number of generations that the parallel hill climber goes through
- populationSize: The size of the population per iteration
- maxLinks: the maximum amount of links that a randomly generated creature could have
- motorJointRange: the range that the joints could move on each motor
- steps: the amount of steps each evaluation goes through

# Body plan and Brain generation
Everything was randomized and initialized in the init function creating a series of matrixes. 

The amount of links is first randomized from 2 to the maximum amount of links permitted as defined in constants.py
Then the following properties were intialized for each link:

- Which link to connect to
- Which side/direction to connect to
- Random Joint location deviation from the center
- Random Joint axis to revolute on
- Random size of the link
- Random location of the center of the link (relative to the Joint)
- Random probability to have a sensor at the link (80%) [colored green]
- Random probability to have a motor at the link (80%)

Then the weights of the synapses were randomized in a fashion similar to the previous tasks.
All the sensors and motors are fully connected.

# Mutations
Everything that was initialized in the generation could be mutated simulatenously with a different probability.

60% probability to alter one of the synapse weights
20% probability to alter one of the link's size / joint position / center position / which link it is connected to
5% probability to alter one of the link's direction and axis of revolute

These probability are purely arbitrary, and is decided from least disruptive to most.

# 5 fitness curves of a population of 25 over 25 generations
![Figure_1](https://user-images.githubusercontent.com/53017682/216672148-44d7b5f5-08d4-4861-89e8-77292c6ab0db.png)
This was created by running 5 simulations of population 25 and generation 25 whilst keeping track of the best fitness of each generation

# Resources and citations
ludobots reddit page: https://www.reddit.com/r/ludobots/
pyrosim github: https://github.com/ccappelle/pyrosim

