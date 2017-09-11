from util.util import *


class Classifier(object):

    def __init__(self, training_set_size):
        self.epsilon = 0.00000000000000000001
        self.training_set_size = training_set_size

    # Classify whether a mushroom belongs to, in this case, the "p" or "e" classification.
    # By going through all the features, one by one, and testing what the highest total probabilityLog is,
    # then overwriting this if higher probabilityLog has been found for another classification.
    # This means the first check will always succeed,
    # and then every consecutive check is checked against the previous best one.
    # When the highest probability for a classification has been established,
    # that classification is given to the mushroom and passed on as the "correct" classification.
    # This is done by taking the log() of the classification count divided by the total, added to the sum of log()
    # of the frequency of the feature for that classification divided by the
    # total of the classification count, of each feature.
    # In the case of the feature having 0 occurrences for a classification, epsilon will be used instead.
    # https://www.youtube.com/watch?v=mFaxEvc1Jr0
    # In the case of a feature not existing in the feature list, we skip it!
    # https://www.youtube.com/watch?v=EqjyLfpv5oA
    def classify(self, obj, features, general_classification_map):
        best_probability = float("-infinity")
        best_classification = None

        for key in general_classification_map:
            classification = general_classification_map[key]
            probability = self.initial_probability(general_classification_map[key])
            probability += self.calc_total_probability(obj, features, classification)

            if probability > best_probability:
                best_probability = probability
                best_classification = classification
        return best_classification

    # Calculate the initial probability, by using the total frequency of the
    # total classification and the size of the training set.
    def initial_probability(self, classification):
        return probability_logarithmic(classification.get_frequency(), self.training_set_size)

    # Calculate the probability of all features combined.
    def calc_total_probability(self, obj, features, classification):
        sum_val = 0
        i = 0
        while i < len(obj):
            for f in features:
                if f.get_name() == obj[i] and f.get_index() == i:
                    sum_val += self.calc_probability(f, classification)
            i += 1
        return sum_val

    # If the feature has a classification (it existed in the training set), increment the probabilityLog based on that.
    # Otherwise, increment the probabilityLog by epsilon.
    def calc_probability(self, feature, classification):
        if feature.has_classification(classification):
            return probability_logarithmic(feature.get_classification_frequency(classification),
                                           classification.get_frequency())
        else:
            return probability_logarithmic(self.epsilon, classification.get_frequency())
