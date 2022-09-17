import numpy as np
import torch
from sklearn import datasets
import torch.nn as nn
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
dataset = datasets.load_iris()
print(dataset.keys())
print(dataset['data'])