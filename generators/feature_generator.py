from objects.feature import *


class FeatureGenerator(object):

    # Checks if a feature exists.
    # If not, add that feature and then move on to check how many times it occurs for our classifications
    # Finally, increment the feature's classification count each time it's found.
    def create(self, data_set, general_classification_map, target_classification):
        features = list()

        for a in data_set:
            i = 0
            while i < len(a):
                if not i == target_classification:
                    feature = Feature(a[i], i)
                    classification = general_classification_map.get(a[target_classification])

                    if not self.feature_exists(features, feature):
                        feature.add_to_classification_dict(classification)
                        features.append(feature)
                    else:
                        found_feature = self.get_feature_from_features(features, feature)
                        if found_feature.has_classification(classification):
                            found_feature.increment_classification_frequency(classification)
                        else:
                            found_feature.add_to_classification_dict(classification)
                i += 1
        return features

    # Checks if said feature exists.
    def feature_exists(self, features, feature):
        for f in features:
            if f.get_name() == feature.get_name() and f.get_index() == feature.get_index():
                return bool(1)
        return bool(0)

    # Return a feature if it exists.
    def get_feature_from_features(self, features, feature):
        for f in features:
            if f.get_name() == feature.get_name() and f.get_index() == feature.get_index():
                return f
