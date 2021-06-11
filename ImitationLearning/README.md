# Assignment - Imitation Learning
The goal of this assignment is to experiment with imitation learning - direct behavior cloning and
the DAgger algorithm, on OpenAI Gym's CarRacing-v0 environment.

## Instructions

Follow the [general instructions](../README.md) to clone the repository. <br>
Specific instructions may be found in the comments in each script.

### Installing Dependencies

1. Required Libraries
    ```bash
    pip3 install -r requirements.txt
    ```
2. Installing resources for the environment. 
    ```bash
    git clone https://github.com/openai/gym.git
    cd gym
    pip install -e .
    pip3 install -e '.[box2d]'
    ```

### Creating the Expert Policy

*Note : This will work only on a local machine*

A small dataset of expert behaviour is already present in [data/data.pkl.gzip](data/data.pkl.gzip).
You are, however encouraged to create your own dataset by running [manual.py](manual.py).

### Defining the model

Edit [model.py](model.py) to add data processing, if required and define your agent model.

### Training

Train your agent by defining the training pipelines in [train.py](train.py) for -

* Naive Behavioral Cloning
* DAgger

Run the training script : 

```txt
usage: train.py [-h] [--mode {naive,dagger}]

optional arguments:
  -h, --help            show this help message and exit
  --mode {naive,dagger}, -m {naive,dagger}
                        Sets the training mode. Default : naive
```

### Evaluation

Add the commands for loading and getting predictions from your trained model in [eval.py](eval.py) and run the script. <br>
*Note : rendering in colab can only be achieved by plotting the state returned with `env.render(mode='rgb_array')`.*
```txt
usage: eval.py [-h] [--render] [--num_episodes NUM_EPISODES]

    optional arguments:
    -h, --help            show this help message and exit
    --render, -r          To visualise the agent's performance
    --num_episodes NUM_EPISODES, -n NUM_EPISODES
                            Number of episodes to run.
```

