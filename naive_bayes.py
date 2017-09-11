from generators.general_classification_generator import *
from generators.feature_generator import *
from util.data_set_parser import *
from classifier import *


class NaiveBayes(object):

    def __init__(self):
        target_classification = 0
        seed = 1
        training_set_percentage = 0.33
        data_loc = "data/mushrooms.csv"

        data_set = obtain_data(data_loc)
        header = data_set[0]
        data_set = data_set[1:]
        training_set = obtain_training_set(data_set, training_set_percentage, seed)

        classification_generator = GeneralClassificationGenerator()
        general_classification_dict = classification_generator.create(training_set, target_classification)

        feature_generator = FeatureGenerator()
        features = feature_generator.create(training_set, general_classification_dict, target_classification)

        self.accuracy_test(header, len(training_set), features, general_classification_dict, data_set)

    # Writes the resultset to a text file, calculates the percentage correctness, a bunch of stuff.
    def accuracy_test(self, header, training_set_size, features, general_classification_dict, data_set):
        correct = 0

        classifier = Classifier(training_set_size)
        delete_old_results()
        text_file = open("res/result.txt", "w")
        text_file.write("prediction" + ", ")
        text_file.write("correct" + ", ")
        for a in header:
            text_file.write(a + ", ")
        text_file.write("\n")
        for a in data_set:
            classification = classifier.classify(a, features, general_classification_dict)
            if classification.get_name() == a[0]:
                text_file.write(classification.get_name() + ", YES")
                correct += 1
            else:
                text_file.write(classification.get_name() + ", NO")
            for val in a:
                text_file.write(", " + val)
            text_file.write("\n")
        text_file.close()
        percentage = (correct / len(data_set))
        print("Naive Bayes accuracy: {}%".format(percentage))

NaiveBayes()
