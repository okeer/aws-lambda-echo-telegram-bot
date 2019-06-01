import pickle


class ClassifierWrapper(object):
    def __init__(self, model_filename):
        with open(model_filename, 'rb') as file:
            self.model = pickle.load(file)

    def classify(self, image_feature_vector):
        return self.model.predict(image_feature_vector)
