import csv
import random
import math


# Read the csv file to obtain its data
def obtain_data(data_loc):
    with open(data_loc, 'rt') as f:
        reader = csv.reader(f)
        return list(reader)


# Return a chunk of the initial data set as a training set.
# This chunk can be seeded to return the exact same random training set.
def obtain_training_set(shuffle_data, percentage, seed):
    random.seed(seed)
    random.shuffle(shuffle_data)
    return shuffle_data[:math.floor(len(shuffle_data) * percentage)]
