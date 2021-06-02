"""
Functions you need to edit in this script:
    - run_episode : preprocessing and action prediction
    - main : load model

How to run this module-
    eval.py [-h] [--render] [--num_episodes NUM_EPISODES]

    optional arguments:
    -h, --help            show this help message and exit
    --render, -r          To visualise the agent's performance
    --num_episodes NUM_EPISODES, -n NUM_EPISODES
                            Number of episodes to run.
"""

from datetime import datetime
import numpy as np
import gym
import os
import json
from model import preprocessing, <MODEL_CLASS> 

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--render", '-r', action='store_true', default=False, help = "To visualise the agent's performance")
parser.add_argument("--num_episodes", '-n', type = int, help = "Number of episodes to run.")
args = parser.parse_args()
RENDER = args.render
NUM_EPISODES = args.num_episodes


def run_episode(env, agent, rendering=True, max_timesteps=2000):
    
    episode_reward = 0
    step = 0
    render_mode = 'human' if rendering else 'rgb_array'

    state = env.reset()
    while True:
        
        # preprocess
        state = ...

        # get action
        a = ...

        next_state, r, done, info = env.step(a)   
        episode_reward += r       
        state = next_state
        step += 1
        env.render(mode = render_mode)

        if done or step > max_timesteps: 
            break

    return episode_reward


def main():
    # load agent
    agent = ... # Initialise model
    agent_name = "" # Distinguish btw naive and dagger
    ... # Load model weights

    env = gym.make('CarRacing-v0').unwrapped

    episode_rewards = []
    for i in range(NUM_EPISODES):
        episode_reward = run_episode(env, agent, rendering=RENDER)
        episode_rewards.append(episode_reward)

    # save results in a dictionary and write them into a .json file
    results = dict()
    results["episode_rewards"] = episode_rewards
    results["mean"] = np.array(episode_rewards).mean()
    results["std"] = np.array(episode_rewards).std()
 
    fname = f"results/{agent_name}-%s.json" % datetime.now().strftime("%Y%m%d-%H%M%S")
    
    with open(fname, "w") as file:
        json.dump(results, file)   
             
    env.close()

if __name__ == "__main__":
    main()