from objects.classification import *
from util.util import *


class GeneralClassificationGenerator(object):

    # Obtain the amount of classifications (In this case, poisonous and not-poisonous, "p" and "e" respectively).
    # Then count the amount of each in the dataSet, and save the frequency for each classification.
    def create(self, data_set, target_classification):
        classification_dict = dict()

        for a in data_set:
            if not (self.increment_classification_frequency(a[target_classification], classification_dict)):
                classification_dict.update({a[target_classification]: Classification(a[target_classification])})
        return classification_dict

    # Increment the frequency of a classification if it has been found.
    def increment_classification_frequency(self, classification, classification_dict):
        if key_exists_in_dict(classification, classification_dict):
            classification_dict[classification].increase_frequency()
            return bool(1)
        return bool(0)
