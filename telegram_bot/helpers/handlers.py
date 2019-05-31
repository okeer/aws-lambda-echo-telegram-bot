from telegram.ext import ConversationHandler, MessageHandler, Filters, CommandHandler
from resources.constants import *


class CustomConvHandler(ConversationHandler):
    SELECTOR = 0

    @staticmethod
    def start(bot, update):
        update.message.reply_text(START_MESSAGE)
        return CustomConvHandler.SELECTOR

    @staticmethod
    def photo(bot, update):
        bot.send_photo(chat_id=update.message.chat.id, photo=max(update.message.photo, key=lambda x: x.file_size))
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
