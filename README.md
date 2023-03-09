# ArtificalLife
run the search.py file to run parallel hill climber evolution with both body and brain mutations training the body to move away from the camera

# Project Goals
There are two main goals that I am going to evaluate in the project:
1. Catastrophe (combination of breadth and depth random search in evolution):
- when a certain number of generation passes without a increase in fitness, the less fit half of the population would be killed and replaced by the better fitting half.
- trying to see whether or not implementing both breadth and depth search outperforms just parallel hill climber


2. Brain vs Morphology change over time
- trying to see the difference between average changes in the brain (nerual network weights) and the morphology (body plan) over the generations

# Methods
The goals of this project is done by performing four main search iterations with the following adjustments:

1. Normal parallel hill climber of a population of 256 for 38 generations
2. Normal parallel hill climber of a population of 256 for 38 generations; alternating brain/body mutations each time the population stagnates
3. Parallel hill climber with catastrophes of a population of 256, capping the maximum simulations at 10,000
4. Parallel hill climber with catastrophes of a population of 256, capping the maximum simulations at 10,000; alternating brain/body mutations each catastrophe

The ones without specifications on the mutations have a free choice of randomizing whether to mutate body or brain.

# Constants that could be changed in constants.py
- maxGen: The maximum number of generations that the parallel hill climber goes through
- numberOfStagnation: The number of stagnating evolution required before a catastrophe happens
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

# Diagrams of Generation
Body Plan Generation:
![Figure_3](https://github.com/Dylan920424/ArtificalLife/blob/final/IMG_0846.jpg)

Brain Generation:
![Figure_2](https://github.com/Dylan920424/ArtificalLife/blob/final/IMG_0845.jpg)


# Mutations
Everything that was initialized in the generation could be mutated simulatenously with a different probability.

50% probability to perform a brain mutation: 
- to alter one of the synapse weights

50% probability to perform a body mutation:
- 20% probability each to alter one of the link's size / joint position / center position / which link it is connected to
- 10% probability to alter one of the link's direction and axis of revolute
- 10% probability to randomly add a new link

These probability are purely arbitrary, and is decided from least disruptive to most.
When the mutations are alternating, only the probability within brain/body matters

Mutation Figures:
![Figure_7](https://github.com/Dylan920424/ArtificalLife/blob/f86cee71da0628b40971c4fdda5d19b8e1fa8d44/IMG_0920.jpg)

# Evolution Figures for Demonstration:
![Figure_8](https://github.com/Dylan920424/ArtificalLife/blob/f86cee71da0628b40971c4fdda5d19b8e1fa8d44/IMG_0921.jpg)

# Graphs
For the following graphs, the left side is the fitness graph, with the generations on the x-axis and the fitness score on the y-axis.
The right side is the average morphological and brain change graph, with the generations on the x-axis and the average number of changes on the y-axis, with the morpholgical changes in blue and the brain changes in red.

# Normal parallel hill climber of a population of 256 for 38 generations
![Figure_1](https://github.com/Dylan920424/ArtificalLife/blob/f86cee71da0628b40971c4fdda5d19b8e1fa8d44/PHCmorphoVbrain.png)

# Normal parallel hill climber of a population of 256 for 38 generations; alternating brain/body mutations each time the population stagnates
![Figure_4](https://github.com/Dylan920424/ArtificalLife/blob/f86cee71da0628b40971c4fdda5d19b8e1fa8d44/SwitchBodyVBrain.png)

# Parallel hill climber with catastrophes of a population of 256, capping the maximum simulations at 10,000
![Figure_5](https://github.com/Dylan920424/ArtificalLife/blob/f86cee71da0628b40971c4fdda5d19b8e1fa8d44/cat_wo_switch.png)

# Parallel hill climber with catastrophes of a population of 256, capping the maximum simulations at 10,000; alternating brain/body mutations each catastrophe
![Figure_6](https://github.com/Dylan920424/ArtificalLife/blob/f86cee71da0628b40971c4fdda5d19b8e1fa8d44/brainVbody.png)

# Conclusion
Based on the four simulations ran, there are two conclusions that could be drawn, answers the two questions posed for this project.

1. For both simulations that utilized the catastrophe method, the final fitness in general reaches a higher value than the ones without. So there may be a increase in efficiency for the method, but more simulations for a longer period of time would be required to form a more concrete conclusion.

2. With the current setting of the mutations, there are no clear difference between the average changes in morphology and brain weights. However, when the alternating method is not utilized, the average changes in morphology is slightly higher than the brain, and when it is utilized the average of both is around the same.

# Future Recommendations & Limitations
For question 1, the main recommendation would be to run the simulation for more seeds and for a longer time to make sure that the results are not purely random and by chance. For question 2, it would be interesting to test the same hypothesis with a more disruptive mutation method as the current method is quite tame for body mutation.

# Resources and citations
ludobots reddit page: https://www.reddit.com/r/ludobots/
pyrosim github: https://github.com/ccappelle/pyrosim

