import os
import unittest
import pickle
import traceback

from dnnclassifier.utils.DataLoader import image_to_np_array
from dnnclassifier.NeuralNetwork import NeuralNetwork


class ClassifierTestCase(unittest.TestCase):
    def test_givenFile_whenRecognize_shouldReturnClass(self):
        try:
            with open(os.environ["IMAGE"], 'rb') as image_file, open(os.environ["MODEL"], 'rb') as model_file:
                model = pickle.load(model_file)
                self.assertIsNotNone(model)

                image = image_to_np_array(image_file, 300, 300)
                rc = ClassifierWrapper(model)
                cls = rc.classify(image)

                self.assertEqual(1, cls)
        except Exception as e:
            traceback.print_exc()


if __name__ == '__main__':
    unittest.main()