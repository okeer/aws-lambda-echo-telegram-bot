from telegram.ext import ConversationHandler, MessageHandler, Filters, CommandHandler
from resources.constants import *
from helpers.classifierwrapper import ClassifierWrapper
import os
import io

from dnnclassifier.utils.DataLoader import image_to_np_array


class CustomConvHandler(ConversationHandler):
    SELECTOR = 0
    WRAPPER = ClassifierWrapper(os.environ["MODEL"])

    @staticmethod
    def __convert_photosize_to_file(photosize):

        return bytes

    @staticmethod
    def start(bot, update):
        update.message.reply_text(START_MESSAGE)
        return CustomConvHandler.SELECTOR

    @staticmethod
    def photo(bot, update):
        bytes = io.BytesIO()
        file = bot.get_file(update.message.photo[-1].file_id)
        file.download(out=bytes)
        image = image_to_np_array(bytes, 64, 64)/255.
        cls = CustomConvHandler.WRAPPER.classify(image)
        update.message.reply_text("Looks like this is a cat with {0} probability".format(cls))
        return CustomConvHandler.SELECTOR

    @staticmethod
    def text(bot, update):
        update.message.reply_text(update.message.text)
        return CustomConvHandler.SELECTOR

    @staticmethod
    def cancel(bot, update):
        update.message.reply_text(CANCEL_MESSAGE)
        return ConversationHandler.END

    def __init__(self):
        super().__init__(
            entry_points=[CommandHandler('start', CustomConvHandler.start)],

            states={
                CustomConvHandler.SELECTOR: [MessageHandler(Filters.photo, CustomConvHandler.photo),
                                             MessageHandler(Filters.text, CustomConvHandler.text)]
            },

            fallbacks=[CommandHandler('cancel', CustomConvHandler.cancel)]
        )
