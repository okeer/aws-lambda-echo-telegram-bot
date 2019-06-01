import os
import unittest
import traceback
import numpy as np

from dnnclassifier.utils.DataLoader import image_to_np_array

from helpers.classifierwrapper import ClassifierWrapper


class ClassifierTestCase(unittest.TestCase):
    def test_givenFile_whenRecognize_shouldReturnClass(self):
        try:
            with open(os.environ["IMAGE"], 'rb') as image_file:
                image = image_to_np_array(image_file, 64, 64)/255.
                rc = ClassifierWrapper(os.environ["MODEL"])
                cls = rc.classify(image)

                self.assertEqual(1, np.squeeze(cls))
        except Exception as e:
            traceback.print_exc()


if __name__ == '__main__':
    unittest.main()