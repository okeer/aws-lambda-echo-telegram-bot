import pickle
import boto3
import numpy as np

from helpers.converters import convert_bytes_to_image_array


class ClassifierWrapper(object):
    pass


class NumdlWrapper(ClassifierWrapper):
    NAME = 'numdl'

    def __init__(self, model_filename):
        with open(model_filename, 'rb') as file:
            self.model = pickle.load(file)

    def classify(self, image_bytes):
        image = convert_bytes_to_image_array(image_bytes)
        confidence = np.squeeze(self.model.predict(image))
        return [{'Name': 'cat', 'Confidence': confidence}]


class AWSRecognizerWrapper(ClassifierWrapper):
    NAME = 'AWS Rekognition'

    def __init__(self):
        self.rekognition = boto3.client("rekognition", "eu-west-1")

    def __detect(self, file_bytes):
        image_bytes = file_bytes.getvalue()
        print(len(image_bytes))
        response = self.rekognition.detect_labels(
            Image={
                'Bytes': image_bytes
            },
            MaxLabels=10,
            MinConfidence=90
        )

        print(response)
        return response['Labels']

    def classify(self, image_bytes):
        return self.__detect(image_bytes)
