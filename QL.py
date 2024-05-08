import gym
from utils import save_frames_as_gif
from collections import deque, namedtuple
import random
import numpy as np
import torch.optim as optim
import matplotlib.pylab as plt
import math

env = gym.make("CarRacing-v2", continuous=False)
print("Observation space: ", env.observation_space)
print("Action space: ", env.action_space)

print("- low:", env.observation_space.low)
print("- high:", env.observation_space.high)

print("Action space samples:")
print(np.array([env.action_space.sample() for i in range(10)]))

print("Observation space samples:")
print(np.array([env.observation_space.sample() for i in range(1)]))


# def create_uniform_grid(low, high, bins=(96, 96)):
#     """Define a uniformly-spaced grid that can be used to discretize a space.
    
#     Parameters
#     ----------
#     low : array_like
#         Lower bounds for each dimension of the continuous space.
#     high : array_like
#         Upper bounds for each dimension of the continuous space.
#     bins : tuple
#         Number of bins along each corresponding dimension.
    
#     Returns
#     -------
#     grid : list of array_like
#         A list of arrays containing split points for each dimension.
#     """
#     grid = []
#     for dim in range(len(bins)):
#         splits = np.linspace(low[dim], high[dim], bins[dim] + 1)[1:-1]
#         grid.append(splits)
    
#     print("Uniform grid: [<low>, <high>] / <bins> => <splits>")
#     for l, h, b, splits in zip(low, high, bins, grid):
#         print("    [{}, {}] / {} => {}".format(l, h, b, splits))
#     return grid

# # Assuming you have flattened your image
# low = [0, 0]
# high = [255, 255]
# bins = (96, 96)  # Bins of 96x96
# create_uniform_grid(low, high, bins)

# print("State space samples:")
# print(np.array([env.observation_space.sample() for i in range(1)]))