class Classification(object):

    def __init__(self, name):
        self.name = name
        self.frequency = 1

    def get_name(self):
        return self.name

    def get_frequency(self):
        return self.frequency

    def increase_frequency(self):
        self.frequency += 1
