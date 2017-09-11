from util.util import *


class Feature(object):
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.classification_dict = dict()

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

    def get_classification_dict(self):
        return self.classification_dict

    def get_classification_frequency(self, classification):
        if self.has_classification(classification):
            return self.classification_dict[classification]

    def add_to_classification_dict(self, classification):
        self.classification_dict.update({classification: 1})

    def increment_classification_frequency(self, classification):
        if self.has_classification(classification):
            self.classification_dict[classification] += 1
            return bool(1)
        return bool(0)

    def has_classification(self, classification):
        return key_exists_in_dict(classification, self.classification_dict)
