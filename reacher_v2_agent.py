PATH_TO_ENV = "/home/marco/Dropbox/Data_Science/Udacity/DRLND/deep-reinforcement-learning/p2_continuous-control/v2_Reacher_Linux/Reacher.x86_64"
save_name = "013_final_reacher_agent"
from unityagents import UnityEnvironment
import numpy as np
import torch
from train_agent import train_agent, test_agent
from DDPGAgent import DDPGAgent as Agent
import sys

if __name__=="__main__":
    # Initiate env
    env = UnityEnvironment(file_name=PATH_TO_ENV)
    # get the default brain
    brain_name = env.brain_names[0]
    brain = env.brains[brain_name]

    # reset the environment
    env_info = env.reset(train_mode=True)[brain_name]
    num_agents = len(env_info.agents)
    action_size = brain.vector_action_space_size
    states = env_info.vector_observations
    state_size = states.shape[1]
    
    agent = Agent(state_size=state_size, action_size=action_size,
                  random_seed=4, actor_units=(200,150), critic_units=(200,150))
    
    if len(sys.argv)>=2 and sys.argv[1]=="retrain":
        train_scores = train_agent(agent, env, brain_name, save_name, n_episodes = 200)
    else:
        agent.actor_local.load_state_dict(save_name+"_actor.pth")
        

        
    test_scores = test_agent(agent, env, brain_name, save_name, n_episodes = 100, train_mode = True)
    print("Average Test scores: {:.2f}".format(np.mean(test_scores)))

    env.close()

