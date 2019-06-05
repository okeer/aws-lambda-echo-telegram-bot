import numdl
from numdl.utils.data import image_to_np_array
from helpers.classifierwrapper import ClassifierWrapper

import numpy as np
import os
import io


wrapper = ClassifierWrapper(os.environ["MODEL"])


def download_file(bot, file_id):
    file_bytes = io.BytesIO()
    file = bot.get_file(file_id)
    file.download(out=file_bytes)
    return file_bytes


def convert_bytes_to_image_array(file_bytes):
    return image_to_np_array(file_bytes, 64, 64)/255.


def photo(bot, update):
    file_bytes = download_file(bot, update.message.photo[-1].file_id)
    image = convert_bytes_to_image_array(file_bytes)

    probability = wrapper.classify(image)
    update.message.reply_text(f"This is a cat with {np.squeeze(probability):.2f} probability")
