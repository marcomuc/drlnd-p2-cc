# Project details
The aim of this repository is to provide a solution to Udacity's [DRLND project 2.](https://github.com/udacity/deep-reinforcement-learning/tree/master/p2_continuous-control) The challenge of this programm is to create an agent which is able to act in the reacher environement. Within this environement an agent consisting of an arm with 2 joints needs needs to get its hand to a moving goal position. For each timestep at which the agents hand is in the goal location, the agent earns a reward of +0.1. For more stable learning, a modified version of the environment containing 20 independant but parallel acting agents is used. The environment is considered solved when the agents earns an average total reward of +30 or higher for 100 consecutives episodes.

The possible actions consist of the applying a continous torque between -1 and 1 for each joint. Each of the joints has two degrees of freedom which results in an action space of size 4. The state space has a size of 33 and contains the position, rotion, velocities, angular velocities of the joints and the goal location.

The code of this repository is based on [DDPG pendulum notebook.](https://github.com/udacity/deep-reinforcement-learning/tree/master/ddpg-pendulum) and valuable discussions in the DRRLND slack channel. The repository contains the following files:
* reacher_v2_agent.py - Code to run the agent with the final parameters
* 013_final_recher_agent_actor.pth - weights of the actor network
* 013_final_recher_agent_critic.pth - weights of the critic network (not necessary to run the agent)
* DDPGAgent.py - Implementation of the DDPG Algorithm
* train_agent.py - Auxillary functions to train and test the agent
* Report.md - Report about the training process and the agents performance


# Getting started
The agent itself requires only standard python3, PyTorch and Numpy. 
1. Install [Anaconda](https://www.anaconda.com/download)
2. Clone [Udacitys'DRLND repository(https://github.com/udacity/deep-reinforcement-learning)] and follow the installation instructions.
3. Download the corresponding Unity environment for your system as described [here](https://github.com/udacity/deep-reinforcement-learning/tree/master/p1_navigation#getting-started)
4. Unzip the environment and change the *PATH_TO_ENV* in variable line 1 in reacher_v2_agent.py accordingly.

# Instructions
You have two options:
1. You can run the agent using the provided pre-trained weights and observe how the agents performs over 100 episodes by executing the following command:
*python reacher_v2_agent.py*
2. Alternatively you can retrain the agent yourself. Please note that this overwrites the provided pre-trained weights if you do not modify the code before.
*python reacher_v2_agent.py retrain*
The last option is especially interesting if you want to play with the agent's parameters yourself.
