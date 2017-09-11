import math
import os


# Checks if a key exists within a dictionary
def key_exists_in_dict(key, classification_dict):
    if key in classification_dict:
        return bool(1)
    return bool(0)


# Returns the log of a probability.
def probability_logarithmic(numerator, denominator):
    return math.log(numerator / denominator)


# Deletes the old results file.
def delete_old_results():
    try:
        os.remove("res/result.txt")
    except OSError:
        pass
