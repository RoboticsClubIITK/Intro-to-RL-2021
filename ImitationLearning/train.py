"""
Functions you need to edit in this script - 
    - train_naive()
    - train_dagger()
    - main()
Feel free to define more functions if required.

Usage: train.py [-h] [--mode {naive,dagger}]

optional arguments:
  -h, --help            show this help message and exit
  --mode {naive,dagger}, -m {naive,dagger}
                        Sets the training mode. Default : naive
"""


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--mode", '-m', choices = ['naive', 'dagger'], default='naive', help = "Sets the training mode. Default : naive")
args = parser.parse_args()
MODE = args.mode 

import numpy as np 
import os 
import pickle
import gzip
import matplotlib.pyplot as plt

# Load Dependencies #
...
#####################

from model import MODEL_NAME # Change this to whatever name you've given your model class
from model import preprocessing

def load_data(directory = "./data", val_split = 0.1):
    """
    Loads the data saved after expert runs.
    Input : directory where data.pkl.gzip is located, val_split
    Output : X_train, Y_train, X_val, Y_val (training and validations sets with split determined by `val_split`)
    """
    data_file = os.path.join(directory, 'data.pkl.gzip')
    
    file =  gzip.open(data_file, 'rb')
    data = pickle.load(file)
        
    X = np.array(data["state"]).astype('float32')
    y = np.array(data["action"]).astype('float32')

    # split data into training and validation sets
    num_samples = len(data["state"])
    val_len = int(val_split*num_samples)
    X_train, y_train = X[:-val_len], y[:-val_len]
    X_val, y_val = X[-val_len:], y[-val_len:]
    return X_train, y_train, X_val, y_val


def train_naive(): # add arguments as needed
    """
    Define your training pipeline for naive behavioural cloning. Delete the pass statement once you're done.
    Save your trained model under "agents/naive".
    This function should return the history of your training and validation metrics.
    """
    pass 

def train_dagger(): # add arguments as needed
    """
    Define your training pipeline for naive behavioural cloning. Delete the pass statement once you're done.
    Save your trained model under "agents/dagger".
    This function should return the history of your training and validation metrics.
    """
    pass

def main():
    # Loading the data
    X_train, y_train, X_val, y_val = load_data(directory = "./data", val_split = 0.1) # Feel free to experiment with val_split

    # Apply preprocessing to observations (if any, delete the next two lines otherwise)
    X_train = ...
    X_val = ... 

    # Initialise your model
    agent = ...


    # Training
    if MODE == 'naive':
        # Call train_naive(), save its results in results/naive.
        pass
    else:
        # Call train_dagger, save its results in results/dagger.
        pass

if __name__ == "__main__":
    main()
